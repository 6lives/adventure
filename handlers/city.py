from aiogram import F
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.loader import dp
from location.city import City
from location.shop import Shop
from utils.game import Game
from utils.game_utils import Utils


@dp.message(F.text == "Магазин", StateFilter("city"))
async def shop(message: Message, players: dict, state: FSMContext):
    player = Utils.get_player(message, players)
    await state.set_state('shop')
    player.current_location = Shop
    await message.reply("Вы в магазине, тут пусто", reply_markup=player.current_location.keyboard)


@dp.message(F.text == "Задания", StateFilter("city"))
async def quests(message: Message, players: dict):
    player = Utils.get_player(message, players)
    player.current_location = City
    await message.reply("Здесь будут задания", reply_markup=player.current_location.keyboard)


@dp.message(F.text == "Исцелиться", StateFilter("city"))
async def heal(message: Message, players):
    player = Utils.get_player(message, players)
    player.current_location = City
    await Game.heal(message, player)
