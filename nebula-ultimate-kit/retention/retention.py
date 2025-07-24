
import sqlite3, datetime

def log_session(email):
    conn = sqlite3.connect("chatgpt_sessions.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usage_sessions (
        email TEXT, ts TEXT
    )''')
    c.execute('INSERT INTO usage_sessions VALUES (?, ?)',
              (email, datetime.datetime.now().isoformat()))
    conn.commit()

def calculate_dau():
    conn = sqlite3.connect("chatgpt_sessions.db")
    c = conn.cursor()
    today = datetime.datetime.now().date().isoformat()
    c.execute("SELECT COUNT(DISTINCT email) FROM usage_sessions WHERE ts LIKE ?", (f"{today}%",))
    return c.fetchone()[0]
