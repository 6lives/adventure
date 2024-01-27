from aiogram import Dispatcher

from middlewares.checkAction import CheckAction
from models.player import Player


def register_middleware(dp: Dispatcher, players: {int: Player}):
   dp.message.middleware(CheckAction(players))
