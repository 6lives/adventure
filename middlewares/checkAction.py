from aiogram import BaseMiddleware
import logging
from models.player import Player
from aiogram.types import Message

from utils.game_utils import Utils


class CheckAction(BaseMiddleware):
    def __init__(self, players: Player):
        self.players = players

    async def __call__(self, handler, event: Message, data):
        player = Utils.get_player(event, self.players)
        logging.error(player.fullName + ' нажал ' + event.text)

        if event.text == '/reset':
            await handler(event, data)
            player.inAction = False
            return

        if player.inAction:
            return
        player.inAction = True

        if player.isDead:
            if event.text == 'Возродиться':
                await handler(event, data)
                player.inAction = False
                return
            await event.bot.send_message(event.chat.id, "Вы мертвы. Можно только возродитья")
            player.inAction = False
            return

        await handler(event, data)
        player.inAction = False
