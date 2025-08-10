import telebot
from telebot import types

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("/start")
item2 = types.KeyboardButton("/help")
item3 = types.KeyboardButton("/BMW")
item4 = types.KeyboardButton("/MERCEDES")
item5 = types.KeyboardButton("/VAG")

markup.add(item1, item2, item3, item4, item5)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Приветствую, сотрудник компании **.
Этот бот поможет тебе конвертировать номер детали в удобный для продажи автозапчастей.

Если возникнут трудности - напиши /help''')

    bot.send_message(message.chat.id, """Для начала выбери марку своей машины!

/BMW — конвертация номеров деталей BMW (как старого образца, так и нового)

/MERCEDES — конвертация номера запчасти Mercedes

/VAG - конвертация номеров деталей VAG-Group""")

@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id, '''/start - запуск бота
/BMW - конвертация номеров деталей BMW (как старого образца, так и нового)
/MERCEDES - конвертация номера детали Mercedes
/VAG - конвертация номеров деталей VAG-Group''')

@bot.message_handler(commands=['BMW'])
def welcome_bmw(message):
    sent = bot.send_message(message.chat.id, '''Отправь мне номер детали BMW
Например, 54124567890''')
    bot.register_next_step_handler(sent, bmw)

@bot.message_handler(commands=['MERCEDES'])
def welcome_mercedes(message):
    sent = bot.send_message(message.chat.id, '''Отправь мне номер детали Mercedes
Например, A2056243802''')
    bot.register_next_step_handler(sent, mb)

@bot.message_handler(commands=['VAG'])
def welcome_vag(message):
    sent = bot.send_message(message.chat.id, '''Отправь мне номер детали VAG
Например, 80A567931''')
    bot.register_next_step_handler(sent, vag)

def create_string_with_space_for_bmw(number):
    new_string = [number[0:2], number[2:4], number[4:5], number[5:8], number[8:]]
    new_string = ' '.join(new_string)
    return new_string

def create_string_with_space_for_mb(number):
    new_string = [number[0:1], number[1:4], number[4:7], number[7:9], number[9:]]
    new_string = ' '.join(new_string)
    return new_string

def create_string_with_space_for_vag(number):
    new_string = []
    if len(number) == 9:
        new_string = [number[0:3], number[3:6], number[6:]]
    elif len(number) == 10:
        new_string = [number[0:3], number[3:6], number[6:9], number[9:]]
    elif len(number) == 11:
        new_string = [number[0:3], number[3:6], number[6:9], number[9:]]
    new_string = ' '.join(new_string)
    return new_string

def create_string_with_space_for_new_bmw_oem(number):
    new_string = [number[0:2], number[2:4], number[4:5], number[5:8], number[8:]]
    new_string = ' '.join(new_string)
    return new_string

def choice(message, result):
    bot.send_message(message.chat.id, result)
    bot.send_message(message.chat.id, '''
/BMW - конвертация номеров деталей BMW (как старого образца, так и нового)

/MERCEDES - конвертация номера детали Mercedes-Benz

/VAG - конвертация номеров деталей VAG-Group''')

def translate(code):
    code = code.replace('A', 'А')
    code = code.replace('B', 'В')
    code = code.replace('C', 'С')
    code = code.replace('D', 'Д')
    code = code.replace('E', 'Е')
    code = code.replace('F', 'Ф')
    code = code.replace('G', 'Г')
    code = code.replace('H', 'Н')
    code = code.replace('I', 'И')
    code = code.replace('J', 'Ж')
    code = code.replace('K', 'К')
    code = code.replace('L', 'Л')
    code = code.replace('M', 'М')
    code = code.replace('N', 'Н')
    code = code.replace('O', 'О')
    code = code.replace('P', 'П')
    code = code.replace('R', 'Р')
    code = code.replace('T', 'Т')
    code = code.replace('W', 'В')
    code = code.replace('X', 'Х')
    code = code.replace('Y', 'У')

    return code

def bmw(message):
    result = ''
    list_of_numbers = message.text.split()
    for number in list_of_numbers:
        if any(c.isalpha() for c in number): 
            first = create_string_with_space_for_new_bmw_oem(number)
            second = number[4:]

            result += ', '.join([number, first, second, translate(number), translate(first), translate(second)]) + ', ' + '\n'
        else:
            first = create_string_with_space_for_bmw(number)
            second = number[4:]

            result += ', '.join([number, first, second]) + ', ' + '\n'

    choice(message, result)

def mb(message):
    result = ''
    list_of_numbers = message.text.split()
    for number in list_of_numbers:
        first = create_string_with_space_for_mb(number)
        second = create_string_with_space_for_mb(number)
        third = number

        result += ', '.join([number, first, translate(second), translate(third)]) + ', ' + '\n'

    choice(message, result)

def vag(message):
    result = ''
    list_of_numbers = message.text.split()
    for number in list_of_numbers:
        first = create_string_with_space_for_vag(number)
        second = create_string_with_space_for_vag(number)
        third = number

        result += ', '.join([number, first, translate(second), translate(third)]) + ', ' + '\n'

    choice(message, result)

bot.polling(none_stop=True)
