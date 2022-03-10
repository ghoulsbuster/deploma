import telebot


TOKEN = "5245318135:AAGg9yEYwhea8g1iCu-WYaZPMcYTtsU0SS4"

bot = telebot.TeleBot(TOKEN)


def add_numbers():
    """ Команда должна попросить пользователя ввести два числа и сложить их

    Программа просит число, затем еще одно число
    Отправляет пользователю в ответ сумму этих двух чисел
    :return:
    """
    pass


def instruction():
    pass


class CommandContext:
    COMMANDS = {
        "Сложить два числа": add_numbers,
        "Как пользоваться": instruction,
    }


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

    for element in CommandContext.COMMANDS:
        key = telebot.types.KeyboardButton(element)
        keyboard.add(key)

    bot.send_message(message.chat.id, reply_markup=keyboard, text="Выберите опцию")
    bot.register_next_step_handler(message, action_context)


def action_context(message):
    try:
        function_to_exec = CommandContext.COMMANDS[message.text]
        text = function_to_exec()
    except KeyError:
        text = "Выберите опцию на клавиатуре!"
    bot.send_message(message.chat.id, text)
    main_menu(message)


bot.polling(none_stop=True)
