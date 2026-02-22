import telebot
import os
import dotenv

from commands import register_bot_commands

def main() -> int:
    dotenv.load_dotenv()
    bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

    register_bot_commands(bot)

    bot.infinity_polling()

    return 0


if __name__ == "__main__":
    main()