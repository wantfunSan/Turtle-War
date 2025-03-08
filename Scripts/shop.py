from tkinter import *
import sqlite3
from tkinter import filedialog
from tkinter.messagebox import showinfo
import os 
from PIL import Image 

import adapter

conn = sqlite3.connect('Game Data\wallet.bal', check_same_thread=False) #создаём дата базу
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS wallet(
	name TEXT PRIMARY KEY,
	bal INTEGER,
	turtle BOOL,
	bg BOOL)
    ''')

def skin():
	c.execute('SELECT bal FROM wallet WHERE name = ?', ('player',)) #проверяем наличие до этого человека в базе
	bal = c.fetchone()

	if bal is None: #если нет, то присваиваем ей значение 0
		showinfo(title=f"Безуспешно", message=f'Денег не хватает(') #отправляем предупреждение, что не хватает денег на покупку
		return

	elif bal[0] >= 25: #если баланс больше или равен стоимости покупки
		c.execute('UPDATE wallet SET bal = bal - 25 WHERE name = ?', ('player',)) #вычисляем стоимость
		conn.commit()

		adapter.change_shape() #меняем скин
		showinfo(title=f"Успех!", message=f'Из мальчика, я превращаю в черепашку!') #просто рофл
		c.execute('UPDATE wallet SET turtle = True WHERE name = "player"')
		conn.commit()

	elif bal[0] < 25: #если баланс меньше, чем стоимость покупи
		showinfo(title=f"Безуспешно", message=f'Денег не хватает(') #отправляем предупреждение, что не хватает денег на покупку

def get_bal():
	c.execute('SELECT bal FROM wallet WHERE name = ?', ('player',)) #проверяем наличие до этого человека в базе
	bal = c.fetchone()

	if bal is None: #если нет, то присваиваем ей значение 0
		showinfo(title=f"Ваш баланс", message=f'Баланс: 0')
		return

	showinfo(title=f"Ваш баланс", message=f'Баланс: {bal[0]}') #отправляем баланс

def bg():
	c.execute('SELECT bal FROM wallet WHERE name = ?', ('player',)) #проверяем наличие до этого человека в базе
	bal = c.fetchone()

	if bal == None: #если нет, то присваиваем ей значение 0
		bal = 0

	if bal[0] >= 50: #если баланс больше или равен стоимости покупки
		c.execute('UPDATE wallet SET bal = bal - 50 WHERE name = ?', ('player',)) #вычисляем стоимость
		conn.commit()

		filepath = filedialog.askopenfilename(title="Выбор файла", filetypes=[('Images', '*.jpg'), ('Images', '*.png'), ('Images', '*.gif')])
		if filepath != "":
			im1 = Image.open(filepath) 
	
			# after converting the image save to desired 
			# location with the Extersion .png 
			file_name = filepath.split('/')
			print(file_name, len(file_name))
			export_filename = f'Game Data/{file_name[len(file_name)-1][:-4]}.gif'
			adapter.change_bg(export_filename, im1)
		
		showinfo(title=f"Успех!", message=f'Чутка приукрасили!') #просто рофл
		c.execute('UPDATE wallet SET bg = True WHERE name = "player"')
		conn.commit()

	if bal[0] < 50: #если баланс меньше, чем стоимость покупи
		showinfo(title=f"Безуспешно", message=f'Денег не хватает(') #отправляем предупреждение, что не хватает денег на покупку

def open_shop():
	shoping_centre = Tk() #создаём окошко магазина
	shoping_centre.title("Магазин") #даём ему имя
	shoping_centre.geometry("300x250") #задаём масштаб

	bt1 = Button(shoping_centre, text = 'Сделать черепашку - 25 монет', width=25, command=skin).pack(anchor=CENTER,expand=True) #создаём кнопку для покупки
	bt2 = Button(shoping_centre, text = 'Поставить фон - 50 монет', width=25, command=bg).pack(anchor=CENTER,expand=True) #создаём кнопку для покупки


def shop():
	window = Tk() #создаём окошко паузы
	
	window.title("Пауза") #даём ему имя
	window.geometry("300x250") #задём масштаб
	
	bt1 = Button(window, text = 'Показать баланс', width=15, command=get_bal).pack(anchor=CENTER,expand=True) #создаём кнопки выбора действий (показать баланс или войти в магазин)
	bt2 = Button(window, text = 'Магазин', width=10, command=open_shop).pack(anchor=CENTER,expand=True)
	bt3 = Button(window, text = 'Настройки', width=10, command=settings).pack(anchor=CENTER,expand=True)

	

	window.mainloop()