import copy
import logging
import random

from aiogram import F
from aiogram.filters import StateFilter
from aiogram.types import Message

from core.loader import dp
from location.forest import Forest
from models.enemy.enemy import Enemy, ENEMIES
from utils.game import Game
from utils.game_utils import Utils


@dp.message(F.text == "Охотиться", StateFilter("forest"))
async def fight(message: Message, players):
    player = Utils.get_player(message, players)

    if player.hp <= 0:
        await message.reply('У вас недостаточно очков жизни. используйте кнопку воскреснуть')
        return

    player.current_location = Forest
    enemy: Enemy = copy.deepcopy(random.choice(ENEMIES))

    await Game.fight(message, player, enemy)

    player.inAction = False


@dp.message(F.text == "Возродиться", StateFilter("forest"))
async def resurrect(message: Message, players):
    player = Utils.get_player(message, players)
    player.isDead = False

    player.current_location = Forest
    if player.hp <= 0:
        player.hp = player.max_hp
        await message.reply('Очки жизни восстановлены', reply_markup=player.current_location.keyboard)


@dp.message(F.text == "Информация")
async def get_info(message: Message, players):
    player = Utils.get_player(message, players)

    player.current_location = Forest
    await message.reply(player.print_characteristics(), reply_markup=player.current_location.keyboard)
