
import sqlite3, datetime

def init_affiliate_db():
    conn = sqlite3.connect("affiliates.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS affiliates (
        ref_code TEXT, referred_email TEXT, joined_on TEXT, payout_status TEXT
    )''')
    conn.commit()

def track_referral(code, email):
    conn = sqlite3.connect("affiliates.db")
    c = conn.cursor()
    c.execute('''INSERT INTO affiliates VALUES (?, ?, ?, ?)''',
              (code, email, datetime.datetime.now().isoformat(), "pending"))
    conn.commit()
