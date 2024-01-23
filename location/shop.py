from aiogram import F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
import logging

from location.forest import Forest
from main import dp
from utils.game_utils import Utils


class Shop:
    __return = KeyboardButton(text='Назад')
    __buyHealth = KeyboardButton(text='Купить зелье здоровья')
    keyboard = ReplyKeyboardMarkup(keyboard=[[__return, __buyHealth]], resize_keyboard=True)

