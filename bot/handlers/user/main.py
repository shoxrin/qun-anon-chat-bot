from aiogram import Dispatcher

from .test_handlers import test_handlers
from .opros import opros_handlers
from .chat_admin_handler import chat_admin_handlers
from .start_bot_handlers import start_bot_handler

def register_user_handlers(dp: Dispatcher) -> None:
    user_handlers = (
        opros_handlers,
        start_bot_handler,
        #test_handlers,
        #chat_admin_handlers,
    )
    for handler in user_handlers:
        handler(dp)