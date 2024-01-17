import asyncio
import sys
import random
import copy

from dotenv import load_dotenv
import logging
from os import getenv

from aiogram.types import Message
from aiogram import Bot, Dispatcher, Router, types
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
    players[message.from_user.id] = Player(message)
    player = get_player(message)
    player.current_location = Forest
    await message.reply(f'New player created for {message.from_user.full_name}',
                        reply_markup=player.current_location.keyboard)


@dp.message(Command("hunt"))
async def fight(message: Message):
    # TODO: сделать обновление сообщения в котором будет отображаться хп уменьшающееся
    player: Player = get_player(message)
    player.current_location = Forest
    enemy: Enemy = copy.deepcopy(random.choice(ENEMIES))
    if player.hp <= 0:
        await message.reply('You dont have enough health points. use "resurrect button"')
        return
    await message.reply(f'You will fight with {enemy.name}')
    while player.hp > 0 or enemy.hp > 0:
        if player.hp <= 0:
            await message.reply(f'{enemy.name} wins. You are dead')
            return
        player.hit(enemy)
        if enemy.hp <= 0:
            player.level_up()
            player.money += enemy.money
            await message.reply('player wins')
            await message.reply(player.print_characteristics(), reply_markup=player.current_location.keyboard)
            return
        enemy.hit(player)


@dp.message(Command("resurrect"))
async def resurrect(message: Message):
    player = get_player(message)
    player.current_location = Forest
    if player.hp <= 0:
        player.hp = player.max_hp
        await message.reply('Your health is restored', reply_markup=player.current_location.keyboard)
    else:
        await message.reply('You are not dead')


@dp.message(Command("info"))
async def get_info(message: Message):
    player = get_player(message)
    player.current_location = Forest
    await message.reply(player.print_characteristics(), reply_markup=player.current_location.keyboard)


@dp.message(Command("shop"))
async def shop(message: Message):
    player = get_player(message)
    player.current_location = Shop
    await message.reply(f'You have {player.money} gold. \n\nYou can buy a health potion that restores 50 health points. It costs 20 gold',
                        reply_markup=player.current_location.keyboard)

@dp.message(Command("buyhealthpotion"))
async def buy_potion(message: Message):
    player = get_player(message)
    if player.money < 20:
        player.current_location = Shop
        await message.reply('You dont have enough money', reply_markup=player.current_location.keyboard)
    elif player.money >= 20 and player.hp != player.max_hp:
        player.money -= 20
        if player.hp + 50 > player.max_hp:
            player.hp = player.max_hp
        else:
            player.hp += 50
        await message.reply(f'hp added. current hp {player.hp}')
    else:
        await message.reply('You have full hp.',  reply_markup=player.current_location.keyboard)


@dp.message(Command("back"))
async def back(message: Message):
    player = get_player(message)
    player.current_location = Forest
    await message.reply('You are returned to forest', reply_markup=player.current_location.keyboard)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

