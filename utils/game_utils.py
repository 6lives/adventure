from models.player import Player
from aiogram.types import Message


class Utils:

    @staticmethod
    def get_player(message: Message, players) -> Player:
        if not players.get(message.from_user.id, None):
            players[message.from_user.id] = Player(message)
        return players.get(message.from_user.id, None)