import sqlite3
import threading

from tkinter import *


conn = sqlite3.connect('Game Data\wallet.bal', check_same_thread=False) #создаём дата базу
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS wallet(
	name TEXT PRIMARY KEY, 
	bal INTEGER,
    turtle BOOL
	)''')




def start_timer_money():
    timer_add = threading.Timer(30, add_money) #создаём таймер
    timer_add.start() #запускаем его
    
    

def add_money():
    c.execute('SELECT bal FROM wallet WHERE name = ?', ('player',)) #проверяем наличие до этого человека в базе
    bal = c.fetchone()

    if bal == None: #если нет-то создаём его
    	c.execute('INSERT INTO wallet VALUES(?, ?, False)', ('player', 0))
    	conn.commit()

    c.execute('UPDATE wallet SET bal = bal + 5 WHERE name = ?', ('player',)) #добавляем одну монетку
    conn.commit()

    start_timer_money() #заново запускаем таймер