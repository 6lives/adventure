from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class City:
    __to_shop = KeyboardButton(text='Магазин')
    __heal = KeyboardButton(text='Исцелиться')
    __quests = KeyboardButton(text='Задания')
    __locations = KeyboardButton(text='Локации')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__to_shop, __heal, __quests], [__locations]], resize_keyboard=True, is_persistent=True)
    title = 'Город'