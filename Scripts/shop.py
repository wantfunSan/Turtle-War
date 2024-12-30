from tkinter import *
import sqlite3
from tkinter.messagebox import showinfo

import adapter

conn = sqlite3.connect('Game Data\wallet.bal', check_same_thread=False) #создаём дата базу
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS wallet(
	name TEXT PRIMARY KEY, 
	bal INTEGER
	)''')

def skin():
	c.execute('SELECT bal FROM wallet WHERE name = ?', ('player',)) #проверяем наличие до этого человека в базе
	bal = c.fetchone()

	if bal == None: #если нет-то создаём его
		bal = 0

	if bal[0] >= 25:
		c.execute('UPDATE wallet SET bal = bal - 25 WHERE name = ?', ('player',)) #добавляем одну монетку
		conn.commit()

		adapter.change_shape()
		showinfo(title=f"Успех!", message=f'Из мальчика, я превращаю в черепашку!')

	if bal[0] < 25:
		showinfo(title=f"Безуспешно", message=f'Денег не хватает(')

def get_bal():
	c.execute('SELECT bal FROM wallet WHERE name = ?', ('player',)) #проверяем наличие до этого человека в базе
	bal = c.fetchone()

	if bal == None:
		bal = 0

	showinfo(title=f"Ваш баланс", message=f'Баланс: {bal[0]}')

def open_shop():
	shoping_centre = Tk()
	shoping_centre.title("Магазин") #даём ему имя
	shoping_centre.geometry("300x250") #задём масштаб

	bt1 = Button(shoping_centre, text = 'Сделать черепашку - 25 монет', width=25, command=skin).pack(anchor=CENTER,expand=True)

def shop():
	window = Tk()
	
	window.title("Пауза") #даём ему имя
	window.geometry("300x250") #задём масштаб

	def exit_from_shop():
		window.destroy()
		adapter.transition()
	
	bt1 = Button(window, text = 'Показать баланс', width=15, command=get_bal).pack(anchor=CENTER,expand=True)
	bt2 = Button(window, text = 'Магазин', width=10, command=open_shop).pack(anchor=CENTER,expand=True)

	window.protocol("WM_DELETE_WINDOW", exit_from_shop)

	window.mainloop()