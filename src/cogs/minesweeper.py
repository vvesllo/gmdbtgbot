from cogs import bot

from telebot import types
import random

games = {}

async def create_land(new=False, game_id = None,  opened_full=False):
    if new:
        game_id = str(random.randint(10000, 99999))
        values = ['💎'] * 6 + ['💣'] * 3
        random.shuffle(values)
        values_matrix = [values[0:3], values[3:6], values[6:9]]
        opened = []
        games[game_id] = [values_matrix, opened]

    values_matrix = games[game_id][0]
    opened = games[game_id][1]

    reply_markup = types.InlineKeyboardMarkup()

    for position_y in range(3):
        inline_buttons = []
        for position_x in range(3):
            position = str(position_x)+str(position_y)
            if position not in opened:
                text = '?'
            else:
                text = values_matrix[position_x][position_y]
            style = None
            if text == "💣":
                style = "danger"
            if text == "💎":
                style = "success"
            
            if opened_full:
                text = values_matrix[position_x][position_y]
            
            callback_data = f'ms:{game_id}:{values_matrix[position_x][position_y]}:{position_x}:{position_y}'
            if opened_full:
                callback_data = "ms:ignore"

            inline_buttons.append(
                types.InlineKeyboardButton(
                    text=text, 
                    callback_data=callback_data,
                    style=style
                    )
                )
        reply_markup.add(*inline_buttons)
    
    return reply_markup

@bot.message_handler(commands=["ms"])
async def minesweeper_game(message):
    await bot.reply_to(
        message,
        '===========Choice============',
        reply_markup=await create_land(new = True)
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("ms"))
async def minesweeper_game_callback_query(call):
    data = call.data.split(":")
    game_id = data[1]
    if game_id == "ignore":
        await bot.answer_callback_query(
            callback_query_id=call.id,
            text="game over!",
            show_alert=True
        )
        return
    
    value = data[2]
    position_x = data[3]
    position_y = data[4]
    opened = games[game_id][1]

    if position_x+position_y not in opened:
        opened.append(position_x+position_y)
        games[game_id][1] = opened

        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            reply_markup=await create_land(game_id=game_id, opened_full=value == '💣')
        )