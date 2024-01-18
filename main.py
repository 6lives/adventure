import asyncio
import sys
import random
import copy
from models.game import Game

from dotenv import load_dotenv
import logging
from os import getenv

from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command

from location.Forest import Forest
from location.shop import Shop
from models.Player import Player

from models.enemy.enemy import ENEMIES, Enemy

load_dotenv()
TOKEN = getenv("TELEGRAM_TOKEN")

dp = Dispatcher()

players: {int: Player} = {}


def get_player(message: Message) -> Player:
    return players.get(message.from_user.id)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    logging.error(message.from_user.full_name + ' нажал кнопку ')
    players[message.from_user.id] = Player(message)
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True

    player.current_location = Forest
    await message.reply(f'Новый игрок создан для {message.from_user.full_name}',
                        reply_markup=player.current_location.keyboard)
    player.inAction = False


@dp.message(Command("Охотиться"))
async def fight(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Охотиться')
    player: Player = get_player(message)
    if player.inAction:
        return

    if player.hp <= 0:
        await message.reply('У вас недостаточно очков жизни. используйте кнопку воскреснуть')
        return

    player.inAction = True
    player.current_location = Forest
    enemy: Enemy = copy.deepcopy(random.choice(ENEMIES))

    await Game.fight(message, player, enemy)

    player.inAction = False


@dp.message(Command("Возродиться"))
async def resurrect(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Возродиться')
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Forest
    if player.hp <= 0:
        player.hp = player.max_hp
        await message.reply('Очки жизни восстановлены', reply_markup=player.current_location.keyboard)
    else:
        await message.reply('Вы еще не умерли, чтобы возродиться')
    player.inAction = False


@dp.message(Command("Информация"))
async def get_info(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Информация')
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Forest
    await message.reply(player.print_characteristics(), reply_markup=player.current_location.keyboard)
    player.inAction = False


@dp.message(Command("Магазин"))
async def shop(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Магазин')
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Shop
    await message.reply(f'У вас {player.money} золота. \n\nВы можете купить зелье здоровья, которое восстанавливает 50 очков жизни. Оно стоит 20 золота',
                        reply_markup=player.current_location.keyboard)
    player.inAction = False


@dp.message(Command("КупитьЗельеЗдоровья"))
async def buy_potion(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку КупитьЗельеЗдоровья')
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True
    if player.money < 20:
        player.current_location = Shop
        await message.reply('У вас недостаточно денег', reply_markup=player.current_location.keyboard)
    elif player.money >= 20 and player.hp != player.max_hp:
        player.money -= 20
        if player.hp + 50 > player.max_hp:
            player.hp = player.max_hp
        else:
            player.hp += 50
        await message.reply(f'Очки жизней добавлены: {player.hp}')
    else:
        await message.reply('У вас и так максимальное количество здоровья',  reply_markup=player.current_location.keyboard)
    player.inAction = False


@dp.message(Command("Назад"))
async def back(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Назад')
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Forest
    await message.reply('Вы вернулись на поляну', reply_markup=player.current_location.keyboard)
    player.inAction = False


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# TODO: приделать инвентарь, возможность продать айтемы
# TODO: мин макс дамаг врагов/героя
# TODO: уклонения/блоки/удача в бою