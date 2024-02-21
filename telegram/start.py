import telebot

from sheets import write_new_row
from telegram.custom_states import MyStates

bot = telebot.TeleBot("6200939711:AAEXRO9rt1-XZIty2nuY0flKbv12np2yKoc")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
    bot.send_message(message.chat.id, 'Hi, write me a name')
    # bot.reply_to(message, "hi there!")

    # message.chat.title
    # markup = types.ReplyKeyboardMarkup()
    # itembtna = types.KeyboardButton('a')
    # itembtnv = types.KeyboardButton('v')
    # itembtnc = types.KeyboardButton('c')
    # itembtnd = types.KeyboardButton('d')
    # itembtne = types.KeyboardButton('e')
    # markup.row(itembtna, itembtnv)
    # markup.row(itembtnc, itembtnd, itembtne)
    # bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "infoo...")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    write_new_row(message)
    bot.reply_to(message, message.text)
