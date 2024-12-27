import turtle
import random
import time

bot = turtle.Turtle()
bot.up()
bot.goto(20, 0)
bot.down()

def ai(player):
	error = random.randrange(0, 101)

	if error <= 100 and error >= 2:
		sdvg = random.randrange(0, 101)

		if sdvg <= 100 and sdvg >= 6:
			bot.forward(1)
		elif sdvg >= 0 and sdvg <= 1:
			bot.left(180)
		elif sdvg >= 2 and sdvg <= 3:
			bot.left(90)
		elif sdvg >= 4 and sdvg <= 5:
			bot.right(90)

	elif error >= 0 and error <= 1:
		bot.goto(player.xcor() + 2, player.ycor())

	if player.position() == bot.position():
		print(f'Встреча {time.asctime()}')