
import sqlite3, datetime

def log_event(session_id, event_type, detail):
    conn = sqlite3.connect("chatgpt_sessions.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS analytics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER, event_type TEXT, detail TEXT, timestamp TEXT
    )''')
    c.execute('''INSERT INTO analytics (session_id, event_type, detail, timestamp)
                 VALUES (?, ?, ?, ?)''',
              (session_id, event_type, detail, datetime.datetime.now().isoformat()))
    conn.commit()
