import time


class Game:
    @staticmethod
    async def fight(message, player, enemy):
        await message.reply(f'Твой противник: {enemy.name}')
        fight_message = await message.bot.send_message(message.chat.id, f'Игрок: {player.hp}/{player.max_hp}хп\n'
                                                                        f'{enemy.name}: {enemy.hp}/{enemy.max_hp}хп')
        while player.hp > 0 or enemy.hp > 0:
            if player.hp <= 0:
                await message.reply(f'{enemy.name} победил. Вы умерли и потеряли 20% опыта')
                player.dead()
                return

            player.hit(enemy)
            await message.bot.edit_message_text(f'Игрок: {player.hp}/{player.max_hp}хп\n'
                                                f'{enemy.name}: {enemy.hp}/{enemy.max_hp}хп',
                                                fight_message.chat.id,
                                                fight_message.message_id)
            if enemy.hp <= 0:
                await message.bot.send_message(message.chat.id, f'Игрок победил и получил:\nОпыт: {enemy.exp}\nЗолото: {enemy.money}')
                enemy.reward(player)
                is_level_up = player.check_level_up()
                if is_level_up:
                    await message.bot.send_message(message.chat.id, 'Вы получили новый уровень!')
                return

            enemy.hit(player)
            await message.bot.edit_message_text(f'Игрок: {player.hp}/{player.max_hp}хп\n'
                                                f'{enemy.name}: {enemy.hp}/{enemy.max_hp}хп',
                                                fight_message.chat.id,
                                                fight_message.message_id)
            time.sleep(0.2)
