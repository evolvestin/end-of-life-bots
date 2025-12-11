import asyncio
import logging
import sys
from datetime import datetime, timezone

from aiogram import Bot, Dispatcher, Router, types

from services.config import ALLOWED_UPDATES, END_OF_LIFE_MESSAGE, ID_DEV, TOKENS, dev_bot
from services.error_handler import TelegramError
from services.functions import bold, code, html_secure
from services.logger import TelegramLogger

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
)

loggers: dict[int, TelegramLogger] = {}


async def all_messages_handler(message: types.Message, bot: Bot) -> None:
    """Router for message processing logic."""
    logger = loggers.get(bot.id)
    if logger:
        asyncio.create_task(logger.log_message(message))
    if message.chat.id < 0:
        return
    await message.answer(text=END_OF_LIFE_MESSAGE, parse_mode='HTML')


async def chat_member_handler(event: types.ChatMemberUpdated, bot: Bot) -> None:
    """Wrapper to route member events to the correct logger."""
    logger = loggers.get(bot.id)
    if logger:
        await logger.log_chat_member_event(event)


def register_router() -> Router:
    """Registers all handlers into the router."""
    router = Router()

    router.my_chat_member.register(chat_member_handler)
    router.chat_member.register(chat_member_handler)
    router.errors.register(TelegramError(dev_bot).handle_error)
    router.message.register(all_messages_handler)
    return router


async def main() -> None:
    """Main entry point for the bot execution."""
    bots_instances = [Bot(token=t) for t in TOKENS if t]

    if not bots_instances:
        logging.error('No tokens found in .env (TOKENS variable).')
        return

    dispatcher = Dispatcher()
    dispatcher.include_router(register_router())

    counter = 0
    active_bots = []
    start_message_lines = []

    for bot in bots_instances:
        counter += 1
        try:
            bot_me = await bot.get_me()
            bot._me = bot_me
            text = f'@{bot_me.username}'
            loggers[bot.id] = TelegramLogger(bot, bot_me)
            active_bots.append(bot)
        except Exception as e:
            text = f'{bot.id}: {html_secure(e)}'
            logging.error(f'Failed to initialize bot with token ending ...{bot.token[-5:]}: {e}')
        start_message_lines.append(f'{counter}. {text}')

    if not active_bots:
        logging.error('No active bots initialized. Exiting.')
        return

    try:
        header_text = bold(f'End Of Life ({len(active_bots)} bots)')
        body_text = '\n'.join(start_message_lines)
        time_text = code(datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))

        await dev_bot.send_message(
            chat_id=ID_DEV,
            text=f'{header_text}:\n{time_text}\n\n{body_text}',
            parse_mode='HTML',
        )
    except Exception as e:
        logging.error(f'Failed to send startup message: {e}')

    await dispatcher.start_polling(*active_bots, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    asyncio.run(main())
