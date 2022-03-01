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
def sample_project_settings:
    """набор вопросов юзеру. 1. Сколько один человек может площадь здания взять в работу


     4. Сколько получает зп средний проектировщик
     5. Сколько разделов выполняет средний проектировщик
     6. Юзер вводит коэффициент "прибыли", скок он хочет бабла с проекта срубить (итоговая стоимость умножается на этот кэф)

          """
    pass

def project_cost():
    #бот прикидывет стоимость проекта.
    """  2. Список разделов, которые нужно проработать (сопоставляются с шаблоном проджекта).
     3. Мощность объекта (просто чтобы прога выбрала коэффициент стоимости)
     7. Далее прога выводит примерный срок проекта (по количеству разделов и сколько один инженер может разделов взять)
     и стоимость проекта оценочную"""
    pass



def create_projects_list():
"""создается список проектов (уточнить, как именно это сделать)"""
    pass
def add_project():
    """добавить проект в список проектов (запрос его названия, проверка на то, что название не занято)"""
    pass

class CommandContext:
    COMMANDS = {
        "Сложить два числа": add_numbers,
        "Как пользоваться": instruction,
        "Дай деняк": f,
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
    text = CommandContext.COMMANDS[message.text]()
    bot.send_message(message.chat.id, text)
    main_menu(message)


bot.polling(none_stop=True)
