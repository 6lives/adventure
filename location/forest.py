from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Forest:
    __to_hunt = KeyboardButton(text='Охотиться')
    __locations = KeyboardButton(text='Локации')
    __resurrect = KeyboardButton(text='Возродиться')
    __info = KeyboardButton(text='Информация')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__locations, __to_hunt,  __info]], resize_keyboard=True, is_persistent=True)
    title = 'Лес'
    keyboard_dead = ReplyKeyboardMarkup(keyboard=[[__locations, __to_hunt], [__resurrect, __info]], resize_keyboard=True, is_persistent=True)
