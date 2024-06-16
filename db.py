import sqlite3
from datetime import datetime

conn = sqlite3.connect('game.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS games (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time TIMESTAMP
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS games_stat (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER,
    question INTEGER, 
    answer INTEGER,
    FOREIGN KEY (game_id) REFERENCES games(ID)
)''')

def insert_games():
    time_now = datetime.now()
    cur.execute('''INSERT INTO games (start_time) VALUES (?)''', (time_now, ))
    cur.execute('SELECT * FROM games')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()

def insert_games_stat(question_num, answer_num):
    cur.execute('INSERT INTO games_stat (game_id, question, answer) VALUES (?, ?, ?)', (1, question_num, answer_num))
    conn.commit()
