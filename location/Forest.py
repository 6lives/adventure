from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Forest:
    __to_hunt = KeyboardButton(text='Охотиться')
    __to_shop = KeyboardButton(text='Магазин')
    __resurrect = KeyboardButton(text='Возродиться')
    __info = KeyboardButton(text='Информация')
    __heal = KeyboardButton(text='Исцелиться')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__to_shop, __to_hunt], [ __resurrect, __info, __heal]], resize_keyboard=True, is_persistent=True)

