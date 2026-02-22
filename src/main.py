import telebot
import os
import dotenv

import commands
import minesweeper

def main() -> int:
    dotenv.load_dotenv()
    bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

    commands.register(bot)
    minesweeper.register(bot)

    bot.infinity_polling()

    return 0


if __name__ == "__main__":
    main()