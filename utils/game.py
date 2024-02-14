import asyncio
import logging
import time

from models.player import Player


class Game:
    @staticmethod
    async def fight(message, player: Player, enemy):
        await message.reply(f'Твой противник: {enemy.name} {enemy.level} уровня')
        fight_message = await message.bot.send_message(message.chat.id, f'Игрок: {player.hp}/{player.max_hp()}хп\n'
                                                                        f'{enemy.name}: {enemy.hp}/{enemy.max_hp}хп')
        while player.hp > 0 or enemy.hp > 0:
            if player.hp <= 0:
                await message.reply(f'{enemy.name} победил. Вы умерли и потеряли 20% опыта', reply_markup=player.current_location.keyboard_dead)
                player.dead()
                return

            player.hit(enemy)
            await message.bot.edit_message_text(f'Игрок: {player.hp}/{player.max_hp()}хп\n'
                                                f'{enemy.name}: {enemy.hp}/{enemy.max_hp}хп',
                                                fight_message.chat.id,
                                                fight_message.message_id)
            if enemy.hp <= 0:
                await message.bot.send_message(message.chat.id, f'Игрок победил и получил:\nОпыт: {enemy.exp_reward}\nЗолото: {enemy.money_reward}')
                enemy.reward(player)
                is_level_up = player.check_level_up()
                if is_level_up:
                    await message.bot.send_message(message.chat.id, f'Вы получили новый уровень и {player.available_attr_pts} очко характеристик!\n'
                                                                    'Потратьте их в окне информации об игроке')
                return

            if player.check_evade():
                logging.warning('evaded')
                continue
            enemy.hit(player)
            await message.bot.edit_message_text(f'Игрок: {player.hp}/{player.max_hp()}хп\n'
                                                f'{enemy.name}: {enemy.hp}/{enemy.max_hp}хп',
                                                fight_message.chat.id,
                                                fight_message.message_id)
            time.sleep(0.4)

    @staticmethod
    async def heal(message, player):
        wait = int(10 + player.level)
        await message.reply(f'Исцеление займет {wait} секунд и вылечит {player.max_hp()/2} хп', reply_markup=player.current_location.keyboard)
        sleep_string = '🛏️'
        sleep_message = await message.bot.send_message(message.chat.id, sleep_string)
        for i in range(wait):
            if len(sleep_string) >= 6:
                sleep_string = '🛏️'
            sleep_string += 'z'
            await message.bot.edit_message_text(sleep_string, sleep_message.chat.id, sleep_message.message_id)
            await asyncio.sleep(1)
        player.heal(player.max_hp()/2)
        await message.bot.send_message(message.chat.id, f'Игрок исцелен. Здоровье {player.hp}/{player.max_hp()}')
