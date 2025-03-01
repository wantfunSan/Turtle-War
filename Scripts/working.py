import sqlite3
import threading

from tkinter import *

#import with_ai
#import ai

conn = sqlite3.connect('Game Data\wallet.bal', check_same_thread=False) #создаём дата базу
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS wallet(
	name TEXT PRIMARY KEY, 
	bal INTEGER,
    turtle BOOL
	)''')
	

def start_timer():
    timer_add = threading.Timer(30, add_money) #создаём таймер
    timer_add.start() #запускаем его

    #timer_win = threading.Timer(5, win)
    #timer_win.start()

def add_money():
    c.execute('SELECT bal FROM wallet WHERE name = ?', ('player',)) #проверяем наличие до этого человека в базе
    bal = c.fetchone()

    if bal == None: #если нет-то создаём его
    	c.execute('INSERT INTO wallet VALUES(?, ?, False)', ('player', 0))
    	conn.commit()

    c.execute('UPDATE wallet SET bal = bal + 5 WHERE name = ?', ('player',)) #добавляем одну монетку
    conn.commit()

    start_timer() #заново запускаем таймер

'''def win():
    win_win = Tk()

    win_win.title("Победа") #даём ему имя
    win_win.geometry("300x250") #задём масштаб

    player = with_ai
    bot = ai.bot
    print(bot, player)

    def delete(): #функция закрытия окна "Проигрыш" и продолжение игры
        win_win.destroy() #закрываем окно
        player.reset() #ставим игрока на место и удаляем все его рисунки
        bot.reset() #ставим бота на место и удаляем все его рисунки
        bot.up() #поднимаем перо, чтобы при перестановки бота на безопасное место под ним не появлялись линии
        bot.goto(20, 0) #ставим на безопасное место
        bot.down() #опускаем перо, чтобы начало рисовать
        with_ai.dvizh()

    win = Label(win_win, text = 'Вы выйграли!').pack(anchor=CENTER,expand=True) #создаём текст в окне сверху по середине
    button = Button(win_win, text='Ок', width=10, command=delete).pack(anchor=CENTER,expand=True) #создаём кнопку "ок"

    win_win.mainloop() #"залупливаем" данное окошко (по факту открываем его)'''