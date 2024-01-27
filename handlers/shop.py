from aiogram import F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.loader import dp
from location.city import City
from location.shop import Shop
from utils.game_utils import Utils


@dp.message(F.text == "Назад", StateFilter("shop"))
async def back(message: Message, players: dict, state: FSMContext):
    player = Utils.get_player(message, players)
    player.current_location = City
    await state.set_state('city')
    await message.reply(f'Вы вернулись в {player.current_location.title}', reply_markup=player.current_location.keyboard)


@dp.message(F.text == "Купить зелье здоровья", StateFilter("shop"))
async def buy_potion(message: Message, players: dict):
    player = Utils.get_player(message, players)

    if player.money < 20:
        player.current_location = Shop
        await message.reply('У вас недостаточно денег', reply_markup=player.current_location.keyboard)
    elif player.money >= 20 and player.hp != player.max_hp:
        player.money -= 20
        player.heal(50)
        await message.reply(f'Очки жизней добавлены: {player.hp}')
    else:
        await message.reply('У вас и так максимальное количество здоровья',  reply_markup=player.current_location.keyboard)
