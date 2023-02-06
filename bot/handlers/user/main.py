from aiogram import Dispatcher

from .start_bot_handlers import start_bot_handler
from .user_group_handlers import user_group_handlers
from .user_menu_handlers import user_menu_handlers
from .user_find_partner_handlers import user_find_partner_handlers

def register_user_handlers(dp: Dispatcher) -> None:
    user_handlers = (
        start_bot_handler,
        user_menu_handlers,  
        user_group_handlers,
        user_find_partner_handlers,
    )
    for handler in user_handlers:
        handler(dp)
        