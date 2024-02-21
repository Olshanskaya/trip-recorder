import telebot  # telebot

from telebot.handler_backends import State, StatesGroup

from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage()

bot = telebot.TeleBot("TOKEN",
                      state_storage=state_storage)



class MyStates(StatesGroup):
    name = State()
    surname = State()
    age = State()
