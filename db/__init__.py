import sqlite3


class ChatDatabase:
    def __init__(self):
        self.db = sqlite3.connect("server.db")
        self.cursor = self.db.cursor()

    def start_db_settings(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS data_table (key TEXT PRIMARY KEY, value TEXT)''')

    def new_row_db(self, key, value):
        self.cursor.execute("INSERT OR REPLACE INTO data_table (key, value) VALUES (?, ?)", (key, value))
        self.db.commit()

    def get_sheet_by_chat_id(self, chat_id):
        self.cursor.execute("SELECT value FROM data_table WHERE key=?", (chat_id,))
        result = self.cursor.fetchone()
        if result:
            print("Значение:", result[0])
        else:
            print("Ключ не найден.")

        # close connection
        # db.close()
