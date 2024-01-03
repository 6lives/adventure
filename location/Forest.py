from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Forest:
    __to_hunt = KeyboardButton(text='/hunt')
    __to_shop = KeyboardButton(text='/shop')
    __resurrect = KeyboardButton(text='/resurrect')
    __info = KeyboardButton(text='/info')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__to_shop, __to_hunt, __resurrect, __info]], resize_keyboard=True)

