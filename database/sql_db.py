import sqlite3
from contextlib import contextmanager

DATABASE = "workflows.db"

@contextmanager
def get_connection():
    conn = sqlite3.connect(DATABASE)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password_hash TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS workflows (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT,
            content TEXT,
            is_template BOOLEAN,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")

def get_user(username):
    with get_connection() as conn:
        return conn.execute(
            "SELECT * FROM users WHERE username = ?", 
            (username,)
        ).fetchone()
