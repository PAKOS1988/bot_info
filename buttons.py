from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_ru(): #Создаем кнопки для основного меню
    kb=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_aboutUs=KeyboardButton('Коротко о компании')
    btn_partnerssites=KeyboardButton('Наши патнеры')
    btn_tasks=KeyboardButton('Наши специалисты')
    btn_clients=KeyboardButton('Наши клиенты')
    btn_certif = KeyboardButton('Наши сертификаты')
    btn_contact = KeyboardButton('Как связаться')
    btn_locat = KeyboardButton('Как найти')
    kb.row_width=1
    kb.add(btn_aboutUs,btn_tasks,btn_certif)
    kb.row_width=2
    kb.row(btn_clients, btn_partnerssites)
    kb.row(btn_contact, btn_locat)
    return kb

def next(): #Создаем кнопки для перелистывания
    kb=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_nextInfo=KeyboardButton('Далее')
    kb.add(btn_nextInfo)
    return kb

def prev(): #Создаем кнопки для возврата
    kb=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_prev=KeyboardButton('Назад')
    kb.add(btn_prev)
    return kb

def inline_info():
    kb=InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='Наш номер телефона', callback_data='btn1')
    btn2 = InlineKeyboardButton(text='Наша локация', callback_data='btn2')
    btn3 = InlineKeyboardButton(text='Наш бот доставки', url='https://t.me/DO_Delivery_Bot')
    kb.add(btn1,btn2,btn3)
    return kb


