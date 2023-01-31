from aiogram import Dispatcher

from .chat_admin_handler import chat_admin_handlers
from .start_bot_handlers import start_bot_handler
from .user_group_handlers import user_group_handlers
from .user_balance_handlers import user_balnce_handlers
from .user_chat_handlers import user_chat_handlers
from .find_partner_handlers import find_partner_handlers

def register_user_handlers(dp: Dispatcher) -> None:
    user_handlers = (
        start_bot_handler,      
        user_group_handlers,
        user_balnce_handlers,
        user_chat_handlers,
        find_partner_handlers,
        #chat_admin_handlers,
    )
    for handler in user_handlers:
        handler(dp)