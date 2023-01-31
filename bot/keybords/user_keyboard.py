from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,  ReplyKeyboardRemove

def create_user_kb():
    user_kb = ReplyKeyboardMarkup(
        keyboard=[
            [
            KeyboardButton(text='Найти собеседника'),
            KeyboardButton(text='Профиль'),
            ],
            [
                KeyboardButton(text='Топ чатов'),
            ],
            [
                KeyboardButton(text='Команды'),
                KeyboardButton(text='Баланс'),
                KeyboardButton(text='Инфо'),
            ],
            [
                KeyboardButton(text='Закрыть меню', ),
            ],
        ],
        resize_keyboard=True
    )
        
    return user_kb

def create_user_balance_kb():
    pass

def create_group_kb():
    filter_group_kb = InlineKeyboardMarkup(row_width=1)
    
    filter_group_buttons = (
        'Топ 15 чатов', 'Топ кол-во участников',
        'Топ от Lescod',
    )
    
    for buttons in filter_group_buttons:
        filter_group_kb.add(
            InlineKeyboardButton(text=buttons, callback_data='show_top')
        )
        
    return filter_group_kb

return_kb = ReplyKeyboardMarkup().add(KeyboardButton(text='Назад'))