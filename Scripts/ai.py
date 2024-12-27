import turtle

def ai(player):
	bot = turtle.Turtle()

	bot.goto(player.xcor() + random.randrange(10, 30), player.ycor())