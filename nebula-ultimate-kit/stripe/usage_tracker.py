
import sqlite3, datetime

def record_usage(email, tokens):
    conn = sqlite3.connect("chatgpt_sessions.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usage (
        email TEXT, tokens INTEGER, ts TEXT
    )''')
    c.execute('INSERT INTO usage VALUES (?, ?, ?)',
              (email, tokens, datetime.datetime.now().isoformat()))
    conn.commit()
