import asyncio
import sys
import random
import copy
import time

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


def check_state():
    def decorator(func):
        async def wrapper(message: types.Message):
            player = get_player(message)
            if player.inAction == True:
                player.inAction = False
                await func(message)
                player.inAction = True
        return wrapper
    return decorator


def get_player(message: Message) -> Player:
    return players.get(message.from_user.id)


@check_state()
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
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
    # TODO: сделать обновление сообщения в котором будет отображаться хп уменьшающееся
    player: Player = get_player(message)
    if player.inAction:
        return

    if player.hp <= 0:
        await message.reply('У вас недостаточно очков жизни. используйте кнопку воскреснуть')
        return

    player.inAction = True
    player.current_location = Forest
    enemy: Enemy = copy.deepcopy(random.choice(ENEMIES))

    await message.reply(f'Твой противник: {enemy.name}')
    fight_message = await message.bot.send_message(message.chat.id, f'Игрок: {player.hp}/{player.max_hp}хп\n'
                                                    f'{enemy.name}: {enemy.hp}/{enemy.max_hp}хп')
    while player.hp > 0 or enemy.hp > 0:
        if player.hp <= 0:
            await message.reply(f'{enemy.name} победил. Вы умерли')
            player.inAction = False
            return

        player.hit(enemy)
        await message.bot.edit_message_text(f'Игрок: {player.hp}/{player.max_hp}хп\n'
                                                    f'{enemy.name}: {enemy.hp}/{enemy.max_hp}хп',
                                            fight_message.chat.id,
                                            fight_message.message_id)
        if enemy.hp <= 0:
            player.level_up()
            player.money += enemy.money
            await message.bot.send_message(message.chat.id, 'Игрок победил')
            player.inAction = False
            return

        enemy.hit(player)
        await message.bot.edit_message_text(f'Игрок: {player.hp}/{player.max_hp}хп\n'
                                            f'{enemy.name}: {enemy.hp}/{enemy.max_hp}хп',
                                            fight_message.chat.id,
                                            fight_message.message_id)
        time.sleep(0.2)


@check_state()
@dp.message(Command("Возродиться"))
async def resurrect(message: Message):
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


@check_state()
@dp.message(Command("Информация"))
async def get_info(message: Message):
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Forest
    await message.reply(player.print_characteristics(), reply_markup=player.current_location.keyboard)
    player.inAction = False


@check_state()
@dp.message(Command("Магазин"))
async def shop(message: Message):
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Shop
    await message.reply(f'У вас {player.money} золота. \n\nВы можете купить зелье здоровья, которое восстанавливает 50 очков жизни. Оно стоит 20 золота',
                        reply_markup=player.current_location.keyboard)
    player.inAction = False


@check_state()
@dp.message(Command("КупитьЗельеЗдоровья"))
async def buy_potion(message: Message):
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


@check_state()
@dp.message(Command("Назад"))
async def back(message: Message):
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

