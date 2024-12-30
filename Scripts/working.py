import sqlite3
import threading

conn = sqlite3.connect('wallet.bal') #создаём дата базу
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXIST wallet(
	name TEXT PRIMARY KEY, 
	bal INTEGER
	)''')
	

def start_timer():
    timer = threading.Timer(60, add_money) #создаём таймер
    time.start() #запускаем его

def add_money():
    c.execute('SELECT bal FROM wallet WHERE name = ?', ('player',)) #проверяем наличие до этого человека в базе
    bal = c.fetchone()

    if bal == None: #если нет-то создаём его
    	c.execute('INSERT INTO wallet VALUES(?, ?)', ('player', 0))
    	conn.commit()

    c.execute('UPDATE wallet SET bal = bal + 1 WHERE name = ?', ('player',)) #добавляем одну монетку

    stert_timer() #заново запускаем таймер