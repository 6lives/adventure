from models.enemy.enemy import Enemy


class Wolf(Enemy):
    def __init__(self, level: int):
        super().__init__('волк', 30, 1, 1, 1, 1, 10, 20, level)


class Bear(Enemy):
    def __init__(self, level: int):
        super().__init__('медведь', 50, 3, 1, 1, 1, 15, 35, level)


class Squirrel(Enemy):
    def __init__(self, level: int):
        super().__init__('белка', 10, 1, 1, 1, 2, 2, 5, level)


class Badger(Enemy):
    def __init__(self, level: int):
        super().__init__('барсук', 20, 2, 1, 0, 1, 15, 20, level)


class Fox(Enemy):
    def __init__(self, level: int):
        super().__init__('лиса', 20, 1, 3, 1, 2, 15, 18, level)
