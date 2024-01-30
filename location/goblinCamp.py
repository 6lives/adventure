import random
from enum import Enum

from location.forest import Forest
from models.enemy.goblinEnemies import *


class GoblinCamp(Forest):
    title = 'Лагерь гоблинов'
    levels = [10, 15]

    class GoblinCampEnemies(Enum):
        goblinTeen: GoblinTeen = 'goblinTeen'
        goblinTrapper: GoblinTrapper = 'goblinTrapper'
        goblinShaman: GoblinShaman = 'goblinShaman'
        goblinWarrior: GoblinWarrior = 'goblinWarrior'
        goblinWarlord: GoblinWarlord = 'goblinWarlord'

    @staticmethod
    def goblin_camp_factory(enemy: GoblinCampEnemies):
        level = random.randint(GoblinCamp.levels[0], GoblinCamp.levels[1])
        match enemy:
            case enemy.goblinTeen:
                return GoblinTeen(level)
            case enemy.goblinTrapper:
                return GoblinTrapper(level)
            case enemy.goblinWarrior:
                return GoblinWarrior(level)
            case enemy.goblinShaman:
                return GoblinShaman(level)
            case enemy.goblinWarlord:
                return GoblinWarlord()
