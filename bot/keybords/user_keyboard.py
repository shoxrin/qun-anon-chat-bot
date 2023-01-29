from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def create_user_kb():
    user_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    
    user_buttons = (
        'Добавить',
        'Баланс',
        'Инфо',
    )

    for user_button in user_buttons:
        user_kb.add(KeyboardButton(text=user_button))
        
    return user_kb