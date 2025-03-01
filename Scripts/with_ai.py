from tkinter import * 
import turtle

import keyboard
import sqlite3 as sql

import ai
import shop

player = turtle.Turtle()
turtle.title('Turtle War') #создаём черепашку

conn = sql.connect('Game Data/wallet.bal', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS wallet(
        name TEXT PRIMARY KEY,
        bal INTEGER,
        turtle BOOL)
    ''')

def dvizh():
    c.execute('SELECT turtle FROM wallet WHERE name="player"')
    have_turtle = c.fetchone()
    if have_turtle is not None and have_turtle[0] == 1:
        player.shape('turtle')
    while True: #бесконечный цикл, дабы не юзать питон 3.9 
        try:  # для того, чтобы не выскакивала ошибка, что нажата другая кнопка
            if keyboard.is_pressed('w') or keyboard.is_pressed('up'):  # идём вперёд при нажатии на "w" или "ц" или на стрелку вверх
                player.forward(1)
                ai.ai(player) #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('s') or keyboard.is_pressed('down'): # поворачиваемся назад при нажатии на "s" или "ы" или на стрелку вниз
                player.left(180)
                ai.ai(player) #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):  # поворачиваемся направо при нажатии на "d" или "в" или на стрелку вправо
                player.right(90)
                ai.ai(player) #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):  # поворачиваемся налево при нажатии на "ф" или "a" или на стрелку влево
                player.left(90)
                ai.ai(player) #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('esc'):  # выходим в магазин при нажатии на "esc"
                shop.shop()#функция открытия магазина
                break #конец итерации
        except:
            continue

