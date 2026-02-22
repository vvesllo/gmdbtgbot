import telebot
import os
import dotenv

from commands import register_bot_commands
from minesweeper import register_bot_minesweeper_game

def main() -> int:
    dotenv.load_dotenv()
    bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))


    register_bot_commands(bot)
    register_bot_minesweeper_game(bot)

    bot.infinity_polling()

    return 0


if __name__ == "__main__":
    main()