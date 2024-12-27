import turtle
import random

bot = turtle.Turtle()

def ai(player):
	error = random.randrange(0, 1)

	if error == 0:
		bot.goto(player.xcor() + 10, player.ycor())
	if error == 1:
		bot.goto(player.xcor() + random.randrange(10, 30), player.ycor())