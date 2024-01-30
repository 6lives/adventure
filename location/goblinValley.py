import random
from enum import Enum

from location.forest import Forest
from models.enemy.goblinEnemies import *


class GoblinValley(Forest):
    title = 'Поляна гоблинов'
    levels = [5, 10]

    class GoblinValleyEnemies(Enum):
        goblinTeen: GoblinTeen = 'goblinTeen'
        goblinTrapper: GoblinTrapper = 'goblinTrapper'
        goblinShaman: GoblinShaman = 'goblinShaman'
        goblinWarrior: GoblinWarrior = 'goblinWarrior'

    @staticmethod
    def goblin_valley_factory(enemy: GoblinValleyEnemies):
        level = random.randint(GoblinValley.levels[0], GoblinValley.levels[1])
        match enemy:
            case enemy.goblinTeen:
                return GoblinTeen(level)
            case enemy.goblinTrapper:
                return GoblinTrapper(level)
            case enemy.goblinWarrior:
                return GoblinWarrior(level)
            case enemy.goblinShaman:
                return GoblinShaman(level)
