from aiogram import F
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from callbacks.levelUpModel import level_up_keyboard
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
    await state.set_state('forest')
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


@dp.message(F.text == "/info")
async def get_info(message: Message, players):
    player = Utils.get_player(message, players)
    if player.available_attr_pts > 0:
        await message.reply(player.print_characteristics(), reply_markup=level_up_keyboard())
        return
    await message.reply(player.print_characteristics())


@dp.message(F.text == "/inventory")
async def get_inventory(message: Message):
    await message.reply('Инвентарь:')
