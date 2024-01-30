from aiogram import F
from aiogram.types import CallbackQuery

from callbacks.levelUpModel import LevelUpCallback, Attribute, level_up_keyboard
from core.loader import dp
from utils.game_utils import Utils


@dp.callback_query(LevelUpCallback.filter(F.attribute))
async def level_up_handler(callback: CallbackQuery, callback_data: LevelUpCallback, players: dict):
    player = Utils.get_player(callback, players)

    if player.available_attr_pts < 1:
        return
    match callback_data.attribute:
        case Attribute.strength:
            player.strength += 1
        case Attribute.agility:
            player.agility += 1
        case Attribute.intelligence:
            player.intelligence += 1
        case Attribute.luck:
            player.luck += 1

    player.available_attr_pts -= 1

    await callback.bot.answer_callback_query(callback.id, f'Вы успешно увеличили характеристику!'
                                             , show_alert=True)
    if player.available_attr_pts < 1:
        await callback.bot.edit_message_text(player.print_characteristics(), callback.message.chat.id,
                                         callback.message.message_id)
    else:
        await callback.bot.edit_message_text(player.print_characteristics(), callback.message.chat.id,
                                             callback.message.message_id, reply_markup=level_up_keyboard())
