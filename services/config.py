import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

TOKENS = [token.strip() for token in os.getenv('TOKENS', '').split(',') if token.strip()]
dev_bot = Bot(token=os.getenv('DEV_TOKEN'))

ID_DEV = int(os.getenv('ID_DEV', 0))
ID_LOGS = int(os.getenv('ID_LOGS', 0))
ID_MEDIA = int(os.getenv('ID_MEDIA', 0))
ID_FORWARD = int(os.getenv('ID_FORWARD', 0))

IGNORE_ERRORS_PATTERN = '|'.join(
    [
        'Backend Error',
        'Read timed out.',
        'Message_id_invalid',
        'Connection aborted',
        'ServerDisconnectedError',
        'Connection reset by peer',
        'is currently unavailable.',
        'returned "Internal Error"',
        'Message to forward not found',
        'Message can&#39;t be forwarded',
        'Failed to establish a new connection',
        'The (read|write) operation timed out',
        'EOF occurred in violation of protocol',
    ]
)

ALLOWED_UPDATES = [
    'callback_query',
    'channel_post',
    'chat_member',
    'edited_channel_post',
    'edited_message',
    'message',
    'my_chat_member',
]

END_OF_LIFE_MESSAGE = (
    '<b>Уведомление о прекращении обслуживания</b>\n\n'
    'Настоящим уведомляем, что эксплуатация и техническая поддержка данного программного обеспечения (бота) '
    'были полностью и окончательно прекращены.\n'
    'Решение о выводе системы из эксплуатации принято в связи с отсутствием фактической востребованности функционала '
    'и целесообразности дальнейшего расходования ресурсов на администрирование.\n'
    'На текущий момент все автоматизированные процессы остановлены, базы данных заархивированы или удалены, '
    'а серверные мощности перераспределены. '
    'Обработка входящих запросов, команд и сообщений более не производится и производиться не будет.\n'
    'По всем вопросам, касающимся архивных данных или причин прекращения работы, '
    f'вы можете направить официальный запрос администратору проекта: {os.getenv("LINK_TO_ADMIN")}.'
)
