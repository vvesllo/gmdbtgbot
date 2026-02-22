import telebot
import random


def register(bot: telebot.TeleBot) -> None:
    @bot.message_handler(commands=["ms"])
    def minesweeper_game(message):
        reply_markup = telebot.types.InlineKeyboardMarkup()

        values = ['o'] * 6 + ['x'] * 3
        random.shuffle(values)

        for position_y in range(3):
            inline_buttons = []
            for position_x in range(3):
                inline_buttons.append(
                    telebot.types.InlineKeyboardButton(
                        text='?', 
                        callback_data=f'ms:{values[position_x + position_y]}'
                        )
                    )
            reply_markup.add(*inline_buttons)

        bot.reply_to(
            message,
            'Choise',
            reply_markup=reply_markup
        )

    @bot.callback_query_handler(func=lambda call: True)
    def minesweeper_game_callback_query(call):
        data = call.data.split(':')
        if data[0] == 'ms':
            value = data[1]

            bot.edit_message_reply_markup(
                call.chat.id,
                call.message.id
            )