from cogs import bot

@bot.message_handler(commands=["start"])
async def start_handler(message):
    await bot.reply_to(
        message,
        "Hello world"
    )
