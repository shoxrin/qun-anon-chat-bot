from aiogram import Dispatcher

from .chat_admin_handler import chat_admin_handlers
from .start_bot_handlers import start_bot_handler
from .user_info_handlers import user_info_handlers

def register_user_handlers(dp: Dispatcher) -> None:
    user_handlers = (
        start_bot_handler,
        user_info_handlers,        
        #chat_admin_handlers,
    )
    for handler in user_handlers:
        handler(dp)