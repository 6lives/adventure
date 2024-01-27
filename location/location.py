from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class LocationSelect:
    __to_forest = KeyboardButton(text='Лес')
    __to_city = KeyboardButton(text='Город')
    __to_valley1 = KeyboardButton(text='Поляна 1')
    __to_valley2 = KeyboardButton(text='Поляна 2')
    __to_valley3 = KeyboardButton(text='Поляна 3')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__to_forest, __to_city], [ __to_valley1, __to_valley2, __to_valley3]], resize_keyboard=True, is_persistent=True)

