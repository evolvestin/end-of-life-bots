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
    '<b>End of Service Notification</b>\n\n'
    'Please be advised that the operation and technical support for this software (bot) '
    'have been fully and permanently discontinued.\n'
    'The decision to decommission the system was reached due to the lack of actual demand '
    'for its functionality and the absence of justification for further resource allocation '
    'towards its administration.\n'
    'Effective immediately, all automated processes have been halted, databases have been archived or deleted, '
    'and server capacity has been reallocated. '
    'Incoming requests, commands, and messages are no longer being processed and will not be addressed.\n'
    'For any inquiries regarding archived data or the rationale behind the service termination, '
    f'you may submit a formal request to the project administrator: {os.getenv("LINK_TO_ADMIN")}.'
)
