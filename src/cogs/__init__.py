import asyncio
from telebot.async_telebot import AsyncTeleBot

import os
import dotenv

dotenv.load_dotenv()
bot = AsyncTeleBot(os.getenv("TELEGRAM_TOKEN"))

from cogs import commands, minesweeper

asyncio.run(bot.infinity_polling())