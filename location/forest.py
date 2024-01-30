import random
from enum import Enum

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from models.enemy.animalEnemies import *


class Forest:
    __to_hunt = KeyboardButton(text='Охотиться')
    __locations = KeyboardButton(text='Локации')
    __resurrect = KeyboardButton(text='Возродиться')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__locations, __to_hunt]], resize_keyboard=True, is_persistent=True)
    title = 'Лес'
    keyboard_dead = ReplyKeyboardMarkup(keyboard=[[__locations, __to_hunt], [__resurrect]], resize_keyboard=True, is_persistent=True)
    levels = [1, 3]

    class ForestEnemies(Enum):
        wolf: Wolf = 'wolf'
        fox: Fox = 'fox'
        bear: Bear = 'bear'
        badger: Badger = 'badger'
        squirrel: Squirrel = 'squirrel'

    @staticmethod
    def forest_factory(enemy: ForestEnemies):
        level = random.randint(Forest.levels[0], Forest.levels[1])
        match enemy:
            case enemy.wolf:
                return Wolf(level)
            case enemy.bear:
                return Bear(level)
            case enemy.fox:
                return Fox(level)
            case enemy.badger:
                return Badger(level)
            case enemy.squirrel:
                return Squirrel(level)
