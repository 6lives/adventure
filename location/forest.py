from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Forest:
    __to_hunt = KeyboardButton(text='Охотиться')
    __locations = KeyboardButton(text='Локации')
    __resurrect = KeyboardButton(text='Возродиться')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__locations, __to_hunt]], resize_keyboard=True, is_persistent=True)
    title = 'Лес'
    keyboard_dead = ReplyKeyboardMarkup(keyboard=[[__locations, __to_hunt], [__resurrect]], resize_keyboard=True, is_persistent=True)
