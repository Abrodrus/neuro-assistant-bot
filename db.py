import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        date TEXT,
        time TEXT,
        created_at TEXT
    )''')
    conn.commit()
    conn.close()

def add_task(user_id, title, date, time):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks (user_id, title, date, time, created_at) VALUES (?, ?, ?, ?, ?)", 
              (user_id, title, date, time, datetime.now()))
    conn.commit()
    conn.close()