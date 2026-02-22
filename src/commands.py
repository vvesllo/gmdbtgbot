import telebot

def register(bot: telebot.TeleBot) -> None:
    @bot.message_handler(commands=["start"])
    def proc_cmd_start(message):
        bot.reply_to(
            message,
            "Hello world"
        )