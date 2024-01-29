from enum import Enum

from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Attribute(str, Enum):
    strength = 'Сила'
    agility = 'Ловкость'
    intelligence = 'Интеллект'
    luck = 'Удача'


class LevelUpCallback(CallbackData, prefix="levelup"):
    attribute: Attribute


def level_up_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in Attribute:
        builder.button(
            text=item,
            callback_data=LevelUpCallback(attribute=item.title()),
        )
    builder.adjust(2, 2)
    return builder.as_markup()
