from tkinter import *
import sqlite3
from tkinter.messagebox import showinfo

import adapter

conn = sqlite3.connect('wallet.bal', check_same_thread=False) #создаём дата базу
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS wallet(
	name TEXT PRIMARY KEY, 
	bal INTEGER
	)''')

def get_bal():
	c.execute('SELECT bal FROM wallet WHERE name = ?', ('player',)) #проверяем наличие до этого человека в базе
	bal = c.fetchone()

	if bal == None:
		bal = 0

	showinfo(title=f"Ваш баланс", message=f'Баланс: {bal[0]}')

def shop():
	window = Tk()
	
	window.title("Магазин") #даём ему имя
	window.geometry("300x250") #задём масштаб

	def exit_from_shop():
		window.destroy()
		adapter.transition()
	
	bt1 = Button(window, text = 'Показать баланс', width=15, command=get_bal).pack(anchor=CENTER,expand=True)
	#bt2 = Button(window, width=10, command=open_shop).pack(anchor=CENTER,expand=True)

	window.protocol("WM_DELETE_WINDOW", exit_from_shop)

	window.mainloop()