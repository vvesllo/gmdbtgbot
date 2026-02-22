from cogs import bot

from telebot import types
import random

@bot.message_handler(commands=["ms"])
async def minesweeper_game(message):
    reply_markup = types.InlineKeyboardMarkup()

    values = ['o'] * 6 + ['x'] * 3
    random.shuffle(values)

    for position_y in range(3):
        inline_buttons = []
        for position_x in range(3):
            inline_buttons.append(
                types.InlineKeyboardButton(
                    text='?', 
                    callback_data=f'ms:{values[position_x + position_y]}'
                    )
                )
        reply_markup.add(*inline_buttons)

    await bot.reply_to(
        message,
        'Choise',
        reply_markup=reply_markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("ms"))
async def minesweeper_game_callback_query(call):
    data = call.data.split(":")
    value = data[1]

    bot.edit_message_reply_markup(
        call.chat.id,
        call.message.id
    )