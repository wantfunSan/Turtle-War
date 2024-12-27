from tkinter import * 
import turtle

import keyboard

def dvizh():
    player = turtle.Turtle() #создаём черепашку

    while True: #бесконечный цикл, дабы не юзать питон 3.9 
        try:  # для того, чтобы не выскакивала ошибка, что нажата другая кнопка
            if keyboard.is_pressed('w'):  # идём вперёд при нажатии на "w" или "ц"
                player.forward(1)
                #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('s'): # поворачиваемся назад при нажатии на "s" или "ы"
                player.left(180)
                #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('d'):  # поворачиваемся направо при нажатии на "d" или "в"
                player.right(90)
                #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('a'):  # поворачиваемся налево при нажатии на "ф" или "a"
                player.left(90)
                #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('esc'):  # выходим в магазин при нажатии на "esc"
                #import shop
                #функция открытия магазина
                break #конец итерации
        except:
            continue