from aiogram import Dispatcher

from .test_handlers import test_handlers

def register_user_handlers(dp: Dispatcher) -> None:
    test_handlers(dp)