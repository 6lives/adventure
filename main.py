import asyncio
import sys
import random
import copy
from models.game import Game
from aiogram import F

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
    if not players.get(message.from_user.id, None):
        players[message.from_user.id] = Player(message)
        message.bot.send_message(message.chat.id, 'Бот был перезапущен, новый игрок создан')
    return players.get(message.from_user.id, None)


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


@dp.message(F.text == "Охотиться")
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


@dp.message(F.text == "Возродиться")
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


@dp.message(F.text == "Информация")
async def get_info(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Информация')
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Forest
    await message.reply(player.print_characteristics(), reply_markup=player.current_location.keyboard)
    player.inAction = False


@dp.message(F.text == "Магазин")
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


@dp.message(F.text == "Купить зелье здоровья")
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
        player.heal(50)
        await message.reply(f'Очки жизней добавлены: {player.hp}')
    else:
        await message.reply('У вас и так максимальное количество здоровья',  reply_markup=player.current_location.keyboard)
    player.inAction = False


@dp.message(F.text == "Назад")
async def back(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Назад')
    player = get_player(message)
    if player.inAction:
        return
    player.inAction = True
    player.current_location = Forest
    await message.reply('Вы вернулись на поляну', reply_markup=player.current_location.keyboard)
    player.inAction = False


@dp.message(F.text == "Исцелиться")
async def heal(message: Message):
    logging.error(message.from_user.full_name + ' нажал кнопку Исцелиться')
    player = get_player(message)
    if player.inAction:
        return
    player.current_location = Forest
    await message.reply('Исцеление займет 10 секунд и вылечит 50 хп', reply_markup=player.current_location.keyboard)
    sleep_string = 'z'
    sleep_message = await message.bot.send_message(message.chat.id, sleep_string)
    for i in range(10):
        if len(sleep_string) >= 4:
            sleep_string = ''
        sleep_string += 'z'
        await message.bot.edit_message_text(sleep_string, sleep_message.chat.id, sleep_message.message_id)
        await asyncio.sleep(1)
    player.heal(50)
    await message.bot.send_message(message.chat.id, 'Игрок исцелен')
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