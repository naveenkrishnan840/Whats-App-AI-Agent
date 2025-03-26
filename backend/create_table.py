import sqlite3


with sqlite3.connect(database="chat_message.db") as conn:
    cursor = conn.cursor()
    cursor.execute("drop table if exists user_login")
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS user_login (
            user_id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            phone_no INT NOT NULL
        );""")
    cursor.execute("drop table if exists whatapp_chat_message")
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS whatapp_chat_message (
            id INTEGER PRIMARY KEY, 
            blob_data BLOB NOT NULL,
            text_data TEXT NOT NULL,
            chat_type TEXT NOT NULL,
            msg_type TEXT NOT NULL,
            chat_time DATETIME NOT NULL,
            user_id INT NOT NULL
        );"""
    )