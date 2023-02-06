from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,  ReplyKeyboardRemove


#Main user menu
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

#Button for opening user menu
open_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Открыть меню'),
        ]
    ],
    resize_keyboard=True
)

#Innline menu for command 'balance'
def create_user_balance_kb():
    balance_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                #InlineKeyboardButton(text='Отправить другу', callback_data='send_money_friend'),
                InlineKeyboardButton(text='Как получать?', callback_data='get_money_info')
            ]
        ]
    )
    
    return balance_kb

#Inline menu for command 'find_chat'
def create_group_kb():
    filter_group_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Топ 15 чатов', callback_data='find_top_fifteen'),
                InlineKeyboardButton(text='Топ от Leskod|Чат бота', callback_data='find_top_on_leskod')
            ],
            [
                InlineKeyboardButton(text='Топ по кол-ву активных участников', callback_data='find_top_active_users')
            ]
        ]
    )
          
    return filter_group_kb

#Inline keyboard to find a partner
def create_find_partner():
    find_partner_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Найти чат', callback_data='find_anonim_chat'),
                InlineKeyboardButton(text='Создать чат', callback_data='create_anonim_chat'),
            ],
            [
                InlineKeyboardButton(text='Отмена', callback_data='cancel_search_anon_chat'),
            ]
        ]
    )
    
    return find_partner_kb

def create_join_partner():
    join_partner_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Соеденить', callback_data='join_anonim_chat'),
                InlineKeyboardButton(text='Найти другого', callback_data='find_anonim_chat'),
            ]
        ]
    )
    
    return join_partner_kb

def create_conn_anon_chat():
    conn_chat_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да!', callback_data='connect_anon_chat'),
                InlineKeyboardButton(text='Нет!', callback_data='close_find_anon_chat')
            ]
        ]
    )
    
    return conn_chat_kb