from tkinter import * 
import turtle

import keyboard

import ai

def dvizh():
    player = turtle.Turtle() #создаём черепашку

    while True: #бесконечный цикл, дабы не юзать питон 3.9 
        try:  # для того, чтобы не выскакивала ошибка, что нажата другая кнопка
            if keyboard.is_pressed('w') or keyboard.is_pressed('up'):  # идём вперёд при нажатии на "w" или "ц" или на стрелку вверх
                player.forward(1)
                ai.test(player)
                #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('s') or keyboard.is_pressed('down'): # поворачиваемся назад при нажатии на "s" или "ы" или на стрелку вниз
                player.left(180)
                #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):  # поворачиваемся направо при нажатии на "d" или "в" или на стрелку вправо
                player.right(90)
                #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):  # поворачиваемся налево при нажатии на "ф" или "a" или на стрелку влево
                player.left(90)
                #движение бота
                continue #следующая итерация
            elif keyboard.is_pressed('esc'):  # выходим в магазин при нажатии на "esc"
                #import shop
                #функция открытия магазина
                break #конец итерации
        except:
            continue