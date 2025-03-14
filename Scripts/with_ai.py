from tkinter import * 
import turtle

import keyboard
import sqlite3 as sql
import random
from tkinter.messagebox import showinfo

import ai
import shop
import working

player = turtle.Turtle()

working.start_timer_money() #запускаем таймер на получение монеток

turtle.title('Turtle War') #создаём черепашку

screen = turtle.Screen()

conn = sql.connect('Game Data/wallet.bal', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS wallet(
		name TEXT PRIMARY KEY,
		bal INTEGER,
		turtle BOOL,
		bg BOOL,
		bg_path TEXT)
	''')

def dvizh(point2win_x, point2win_y):
	showinfo(title=f"Информация", message=f'Твоя победная точка: по оси x:{point2win_x}; по оси y: {point2win_y}')
	c.execute('SELECT turtle, bg FROM wallet WHERE name="player"')
	have_turtle = c.fetchone()
	if have_turtle is not None and have_turtle[0] == 1:
		player.shape('turtle')
	if have_turtle is not None and have_turtle[1] == 1:
		c.execute('SELECT bg_path FROM wallet WHERE name = "player"')
		path2file = c.fetchone()[0]

		screen.bgpic(path2file)
			
	while True:
		try:
			while keyboard.is_pressed('w') or keyboard.is_pressed('up') : #бесконечный цикл, дабы не юзать питон 3.9 
				player.forward(1)
				ai.ai(player, point2win_x, point2win_y) #движение бота
				continue #следующая итерация
			while keyboard.is_pressed('s') or keyboard.is_pressed('down'): # поворачиваемся назад при нажатии на "s" или "ы" или на стрелку вниз
				player.left(180)
				ai.ai(player, point2win_x, point2win_y) #движение бота
			while keyboard.is_pressed('d') or keyboard.is_pressed('right'):  # поворачиваемся направо при нажатии на "d" или "в" или на стрелку вправо
				player.right(90)
				ai.ai(player, point2win_x, point2win_y) #движение бота
			while keyboard.is_pressed('a') or keyboard.is_pressed('left'):  # поворачиваемся налево при нажатии на "ф" или "a" или на стрелку влево
				player.left(90)
				ai.ai(player, point2win_x, point2win_y) #движение бота
			while keyboard.is_pressed('esc'):
				shop.shop(point2win_x, point2win_y)#функция открытия магазина
				break
			while keyboard.is_pressed('b'):
				showinfo(title=f"Информация", message=f'Твоя победная точка: по оси x:{point2win_x}; по оси y: {point2win_y}\nТвои координаты: по оси x:{round(player.xcor())}; по оси y: {round(player.ycor())}') #gps
		except:
			continue
		

def new_point():
	new_point2win_x = random.randrange(1, 366)
	new_point2win_y = random.randrange(1, 366)
	dvizh(new_point2win_x, new_point2win_y)