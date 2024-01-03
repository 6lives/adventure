from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Shop:
    __return = KeyboardButton(text='/back')
    __buyHealth = KeyboardButton(text='/buyhealthpotion')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__return, __buyHealth]], resize_keyboard=True)