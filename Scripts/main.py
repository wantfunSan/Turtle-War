from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # убираем приветственное сообщение от pygame'а

import pygame 
 
sc = pygame.display.set_mode((477, 132), pygame.NOFRAME) #создаём окно pygame'а без панели управления окном
 
download_load = pygame.image.load('.\\Game Data\\download.bmp') #подгружаем фоточку
download_rect = download_load.get_rect() # создается экземпляр Rect
sc.blit(download_load, download_rect) #обобщаем подгрузку
 
pygame.display.update() #открываем окно

import sys
import time
from tkinter import *

pygame.display.quit() #по окончании импортов закрываем окно с фоточкой

def selected(): #функция после выбора режима
	if my_var.get() == 0: #если выбор падёт на игру с ии(оно стоит как 0)
		import with_ai 
		import ai
		root.destroy() #закрываем окно для выбора
		with_ai.dvizh() #запускаем следующую функцию

	elif my_var.get() == 1: #если выбор падёт на игру с другом(оно стоит как 1)
		import with_friend
		root.destroy() #закрываем окно для выбора
		#запускаем следующую функцию

root = Tk() #создаём окно уже tkinter'а
root.title("Выбор режима") #даём ему имя
root.geometry("300x250") #задём масштаб

my_var = IntVar() #задаём переменную для выбора режима
my_var.set(0) #задаём первоначальное значение как 0 (игра с ии)

choose = Label(root, text = 'Выберите Ваш режим игры:').pack(anchor=CENTER,expand=True) #создаём текст в окне сверху по середине
r1 = Radiobutton(root, text='С ботом', variable=my_var, value=0).pack(anchor=CENTER,expand=True) #создаём переключатель в окне чуть ниже текста
r2 = Radiobutton(root, text='С другом', variable=my_var, value=1).pack(anchor=CENTER) #создаём второй ереключатель в окне чуть ниже предыдущего
button = Button(root, text='Подтвердить', width=10, command=selected).pack(anchor=CENTER,expand=True) #создаём кнопку подтверждения действия в окне чуть ниже последнего переключателя

mainloop() #"залупливаем" данное окошко (по факту открываем его)