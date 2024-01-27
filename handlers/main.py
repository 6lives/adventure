from aiogram import F
from aiogram.filters import CommandStart

import logging

from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.loader import dp
from location.forest import Forest
from models.player import Player
from utils.game_utils import Utils


@dp.message(CommandStart())
async def command_start_handler(message: Message, players, state: FSMContext) -> None:
    await state.clear()
    players[message.from_user.id] = Player(message)
    player = Utils.get_player(message, players)

    player.current_location = Forest
    await state.set_state('forest')
    await message.reply(f'Новый игрок создан для {message.from_user.full_name}',
                        reply_markup=player.current_location.keyboard)


@dp.message(F.text == "/reset")
async def command_reset(message: Message, players: dict, state: FSMContext):
    player = Utils.get_player(message, players)
    await state.clear()
    player.current_location = Forest
    await message.reply("State персонажа был сброшен", reply_markup=player.current_location.keyboard)


@dp.message(F.text.startswith("анонс"))
async def announce(message: Message, players: dict):
    if message.from_user.id != 1434291606:
        return
    text = message.text.replace('анонс ', '')
    text = 'Анонс: ' + text
    players_ids: [] = players.keys()
    for i in players_ids:
        await message.bot.send_message(i, text)
