import turtle
import random

bot = turtle.Turtle()

def ai(player):
	error = random.randrange(0, 101)

	print(error)

	if error <= 100 and error >= 2:
		sdvg = random.randrange(0, 101)

		if sdvg >= 16:
			bot.forward(1)
		elif sdvg >= 0 and sdvg <= 5:
			bot.left(180)
		elif sdvg >= 6 and sdvg <= 10:
			bot.left(90)
		elif sdvg >= 11 and sdvg <= 15:
			bot.right(90)

	elif error >= 0 and error <= 1:
		bot.goto(player.xcor(), player.ycor())