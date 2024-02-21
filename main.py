from db import ChatDatabase
from telegram.start import bot

if __name__ == '__main__':
    db_inst = ChatDatabase()
    db_inst.start_db_settings()
    bot.infinity_polling()
