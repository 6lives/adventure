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


@dp.message(F.text == "Магазин")
async def shop(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Магазин')
    player = Utils.get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Shop
    await message.reply(f'У вас {player.money} золота. \n\nВы можете купить зелье здоровья, которое восстанавливает 50 очков жизни. Оно стоит 20 золота',
                        reply_markup=player.current_location.keyboard)
    player.inAction = False


@dp.message(F.text == "Купить зелье здоровья")
async def buy_potion(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку КупитьЗельеЗдоровья')
    player = Utils.get_player(message)
    if player.inAction:
        return
    player.inAction = True
    if player.money < 20:
        player.current_location = Shop
        await message.reply('У вас недостаточно денег', reply_markup=player.current_location.keyboard)
    elif player.money >= 20 and player.hp != player.max_hp:
        player.money -= 20
        player.heal(50)
        await message.reply(f'Очки жизней добавлены: {player.hp}')
    else:
        await message.reply('У вас и так максимальное количество здоровья',  reply_markup=player.current_location.keyboard)
    player.inAction = False


@dp.message(F.text == "Назад")
async def back(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Назад')
    player = Utils.get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Forest
    await message.reply('Вы вернулись на поляну', reply_markup=player.current_location.keyboard)
    player.inAction = False