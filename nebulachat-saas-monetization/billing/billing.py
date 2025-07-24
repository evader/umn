import json, sqlite3

def init_billing():
    conn = sqlite3.connect("chatgpt_sessions.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY, plan TEXT, stripe_id TEXT, joined TEXT
    )''')
    conn.commit()

def upgrade_user(email, new_plan):
    conn = sqlite3.connect("chatgpt_sessions.db")
    c = conn.cursor()
    c.execute('UPDATE users SET plan=? WHERE email=?', (new_plan, email))
    conn.commit()