from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class LocationSelect:
    __to_forest = KeyboardButton(text='Лес')
    __to_city = KeyboardButton(text='Город')
    __to_goblin_valley = KeyboardButton(text='Поляна гоблинов')
    __to_goblin_camp = KeyboardButton(text='Лагерь гоблинов')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__to_forest, __to_city], [__to_goblin_valley, __to_goblin_camp]],
                                   resize_keyboard=True, is_persistent=True)
