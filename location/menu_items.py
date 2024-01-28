from aiogram.types import BotCommand

__reset = BotCommand(command='/start', description='Создание нового персонажа')
__start = BotCommand(command='/reset', description='Сброс персонажа при застревании')
__info = BotCommand(command='/info', description='Отобразить информацию об игроке')
__inventory = BotCommand(command='/inventory', description='Отобразить инвентарь игрока')
menuItems = [__start, __info, __inventory, __reset]
