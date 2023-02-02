from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,  ReplyKeyboardRemove

def create_conn_chat():
    conn_chat_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да!', callback_data='connect_chat'),
                InlineKeyboardButton(text='Нет!', callback_data='close_find_chat')
            ]
        ]
    )
    
    return conn_chat_kb