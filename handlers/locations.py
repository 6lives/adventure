from aiogram import F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.loader import dp
from location.city import City
from location.forest import Forest
from location.goblinCamp import GoblinCamp
from location.goblinValley import GoblinValley
from utils.game_utils import Utils
from location.locations import LocationSelect


@dp.message(F.text == "Локации")
async def locations(message: Message, players: dict, state: FSMContext):
    await state.set_state('locationSelect')
    player = Utils.get_player(message, players)
    player_old_location = player.current_location
    player.current_location = LocationSelect
    await message.reply(f"Вы сейчас на локации {player_old_location.title}. Куда хотите переместиться?", reply_markup=player.current_location.keyboard)


@dp.message(F.text == "Лес", StateFilter("locationSelect"))
async def forest(message: Message, players: dict, state: FSMContext):
    await state.set_state('forest')
    player = Utils.get_player(message, players)
    player.current_location = Forest
    await message.reply(f"Вы пришли в локацию {player.current_location.title}",
                        reply_markup=player.current_location.keyboard)


@dp.message(F.text == "Город", StateFilter("locationSelect"))
async def city(message: Message, players: dict, state: FSMContext):
    await state.set_state('city')
    player = Utils.get_player(message, players)
    player.current_location = City
    await message.reply(f"Вы пришли в локацию {player.current_location.title}",
                        reply_markup=player.current_location.keyboard)


@dp.message(F.text == "Поляна гоблинов", StateFilter("locationSelect"))
async def goblin_valley(message: Message, players: dict, state: FSMContext):
    await state.set_state('goblinValley')
    player = Utils.get_player(message, players)
    player.current_location = GoblinValley
    await message.reply(f"Вы пришли в локацию {player.current_location.title}",
                        reply_markup=player.current_location.keyboard)


@dp.message(F.text == "Лагерь гоблинов", StateFilter("locationSelect"))
async def goblin_camp(message: Message, players: dict, state: FSMContext):
    await state.set_state('goblinCamp')
    player = Utils.get_player(message, players)
    player.current_location = GoblinCamp
    await message.reply(f"Вы пришли в локацию {player.current_location.title}",
                        reply_markup=player.current_location.keyboard)