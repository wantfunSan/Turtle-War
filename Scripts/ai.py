import turtle
import random
import time

from tkinter import *
import perehodnik

bot = turtle.Turtle() #создаём бота

bot.up() #поднимаем перо, чтобы при перестановки бота на безопасное место под ним не появлялись линии
bot.goto(20, 0) #ставим на безопасное место
bot.down() #опускаем перо, чтобы начало рисовать

def ai(player):
	error = random.randrange(0, 101) #создаём область ошибки от 0 до 100

	if error <= 100 and error >= 2: #вероятность выпадения около 98%
		sdvg = random.randrange(0, 101) #создаём область ошибки от 0 до 100

		if sdvg <= 100 and sdvg >= 6: #вероятность выпадения около 94%
			bot.forward(1)            #двигаем бота вперёд
		elif sdvg >= 0 and sdvg <= 1: #вероятность выпадения около 2%
			bot.left(180)            #поворачиваем бота назад
		elif sdvg >= 2 and sdvg <= 3: #вероятность выпадения около 2%
			bot.left(90)            #поворачиваем бота налево 
		elif sdvg >= 4 and sdvg <= 5:#вероятность выпадения около 2%
			bot.right(90)            #поворачиваем бота направо

	elif error >= 0 and error <= 1: #вероятность выпадения около 2%
		bot.goto(player.xcor() + 12, player.ycor()) #ставим бота, для напряжения игрока, недалеко от него на безопасном месте

		##################################### ВСЕ ВЕРОЯТНОСТИ ТРЕБУЮТСЯ, ЧТОБЫ БОТ НЕ ДВИГАЛСЯ, КАК СУМАСШЕДШИЙ, ГОРКАМИ #####################################

	if player.position() == bot.position() or (abs(player.xcor()) - abs(bot.xcor()) <= 10 and abs(player.xcor()) - abs(bot.xcor()) >= 0) and abs(player.ycor()) == abs(bot.ycor()) or (abs(bot.xcor()) - abs(player.xcor()) <= 10 and abs(bot.xcor()) - abs(player.xcor()) >= 0) and abs(player.ycor()) == abs(bot.ycor()) or (abs(player.ycor()) - abs(bot.ycor()) <= 10 and abs(player.ycor()) - abs(bot.ycor()) >= 0) and abs(player.xcor()) == abs(bot.xcor()) or (abs(bot.ycor()) - abs(player.ycor()) <= 10 and abs(bot.ycor()) - abs(player.ycor()) >= 0) and abs(player.xcor()) == abs(bot.xcor()) or (abs(player.ycor()) - abs(bot.ycor()) <= 10 and abs(player.ycor()) - abs(bot.ycor()) >= 0) and (abs(player.xcor()) - abs(bot.xcor()) <= 10 and abs(player.xcor()) - abs(bot.xcor()) >= 0) or (abs(bot.xcor()) - abs(player.xcor()) <= 10 and abs(bot.xcor()) - abs(player.xcor()) >= 0) and (abs(bot.ycor()) - abs(player.ycor()) <= 10 and abs(bot.ycor()) - abs(player.ycor()) >= 0) or (abs(player.ycor()) - abs(bot.ycor()) <= 10 and abs(player.ycor()) - abs(bot.ycor()) >= 0) and (abs(bot.xcor()) - abs(player.xcor()) <= 10 and abs(bot.xcor()) - abs(player.xcor()) >= 0) or (abs(bot.xcor()) - abs(player.xcor()) <= 10 and abs(bot.xcor()) - abs(player.xcor()) >= 0) and (abs(player.ycor()) - abs(bot.ycor()) <= 10 and abs(player.ycor()) - abs(bot.ycor()) >= 0): #дальше идут проверки позиций игрока и бота, лучше Вам самим в этом разобраться, много текста будет)
		root = Tk() #создаём окно уже tkinter'а
		root.title("Проигрыш") #даём ему имя
		root.geometry("300x250") #задём масштаб

		def delete():
			root.destroy()
			player.reset() #ставим игрока на место и удаляем все его рисунки
			bot.reset() #ставим бота на место и удаляем все его рисунки
			bot.up() #поднимаем перо, чтобы при перестановки бота на безопасное место под ним не появлялись линии
			bot.goto(20, 0) #ставим на безопасное место
			bot.down() #опускаем перо, чтобы начало рисовать
			perehodnik.perehod()

		loose = Label(root, text = 'Вы проиграли!').pack(anchor=CENTER,expand=True) #создаём текст в окне сверху по середине
		button = Button(root, text='Ок', width=10, command=delete).pack(anchor=CENTER,expand=True) #создаём кнопку "ок"

		root.mainloop() #"залупливаем" данное окошко (по факту открываем его)