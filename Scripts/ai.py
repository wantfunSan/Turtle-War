import turtle
import random

bot = turtle.Turtle()

def ai(player):
	error = random.randrange(0, 101)

	print(error)

	if error <= 100 and error >= 26:
		bot.goto(player.xcor() + 10, player.ycor())

	elif error >= 0 and error <= 1:
		bot.goto(player.xcor() + random.randrange(10, 30), player.ycor())