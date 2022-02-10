import telebot


TOKEN = "5245318135:AAGg9yEYwhea8g1iCu-WYaZPMcYTtsU0SS4"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def start(message):
    """Checks if user registered or not
    if not, calls register function
    if yes, call main_menu function
    """
    main_menu(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """ The main callback worker,
    checks call_back from every function
    """
    pass


def main_menu(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    key_setup = telebot.types.KeyboardButton(
        text="Настроить скрипт",
    )
    key_about = telebot.types.KeyboardButton(
        text="Как пользоваться?",
    )
    keyboard.add(key_setup)
    keyboard.add(key_about)
    bot.send_message(message.chat.id, reply_markup=keyboard, text="Выберите опцию")

bot.polling(none_stop=True)
