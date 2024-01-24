from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Shop:
    __return = KeyboardButton(text='Назад')
    __buyHealth = KeyboardButton(text='Купить зелье здоровья')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__return, __buyHealth]], resize_keyboard=True)

