import asyncio
import sys
import handlers.main
import handlers.forest
import handlers.locations
import handlers.city
import handlers.shop
import callbacks.levelUpHandler
import handlers.goblinValley
import handlers.goblinCamp

from middlewares import register_middleware
from models.player import Player
from location.menu_items import menuItems

from dotenv import load_dotenv
import logging
from os import getenv

from aiogram import Bot
from aiogram.enums import ParseMode
from core.loader import dp


load_dotenv()
TOKEN = getenv("TELEGRAM_TOKEN")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.set_my_commands(menuItems)
    # And the run events dispatching
    players: {int: Player} = {}
    register_middleware(dp, players)
    await dp.start_polling(bot, players=players)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# TODO: приделать инвентарь, возможность продать айтемы
# TODO: мин макс дамаг врагов/героя
# TODO: уклонения/блоки/удача в бою
# TODO: магазин сделать через инлайн кнопки для этого нужно добавить стейт персонажа дополнительный
# TODO: задания уровня "убить столько то мобов" сделать после инвентаря
# TODO: писать статистику боя и дать ее посмотреть
