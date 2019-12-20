import turtle
import os
import math
import random

# set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bow & Arrow Game")
# wn.bgpic("background.gif")

# Register the Shapes
turtle.register_shape("balloons.gif")
turtle.register_shape("joker.gif")

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()



# create a player
player1 = turtle.Turtle()
player1.color("green")
player1.shape("joker.gif")
player1.penup()
player1.speed(0)
player1.setposition(-275, 0)
player1.setheading(360)

playerspeed = 15




# Choose the number of balloon 
number_of_balloon = 3
# Create an empty list of balloons
balloons = []

# Add balloons to tthe list
for i in range(number_of_balloon):
	# Create the balloon
	balloons.append(turtle.Turtle())

for balloon in balloons:
	balloon.color("red")
	balloon.shape("balloons.gif")
	balloon.penup()
	balloon.speed(0)
	x = random.randint(-100, 270)
	y = random.randint(-270, 0)
	balloon.setposition(x, y)

balloonspeed = 2




# create the player's weapon #arrow
arrow = turtle.Turtle()
arrow.color("yellow")
arrow.shape("arrow")
arrow.penup()
arrow.speed(0)
arrow.setheading(360)
arrow.shapesize(0.2, 0.8)
arrow.hideturtle()

arrowspeed = 30


# Define Arrow state
# ready - ready to fire
# fire - arrow is firing
arrowstate = "ready"




# player1 move
def move_up():
	y = player1.ycor()
	y +=playerspeed
	if y > 270:
		y = 270
	player1.sety(y)

def move_down():
	y = player1.ycor()
	y -=playerspeed
	if y < -270:
		y = -270
	player1.sety(y)


def fire_arrow():
	# Declare arrowstate as a global if it needs changed
	global arrowstate
	if arrowstate == "ready":
		arrowstate = "fire"
		# Move arrow to the just above the player
		x = player1.xcor() + 0
		y = player1.ycor() 
		arrow.setposition(x, y)
		arrow.showturtle()


def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if(distance < 15):
		return True
	else:
		return False


# Keyboard Controls
turtle.listen()
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(fire_arrow, "space")











# main game loop
while True:

	for balloon in balloons:
		# move the balloon
		y = balloon.ycor()
		y +=balloonspeed
		balloon.sety(y)

		# reverse balloon
		# if balloon.ycor() > 280:
		# 	y = balloon.ycor()
		# 	y +=balloonspeed
		# 	balloon.sety(y)

		# if balloon.ycor() < -280:
		# 	y = balloon.ycor()
		# 	y +=balloonspeed
		# 	balloon.sety(y)

		# reverse balloon
		if balloon.ycor() > 280:
			# balloonspeed *= -1
			# balloon.hideturtle()
			x = random.randint(-100, 270)
			y = random.randint(-280, -279)
			balloon.setposition(x, y)

		# if balloon.ycor() < -280:
		# 	balloonspeed *= -1

		if isCollision(arrow, balloon):
			# Reset the arrow
			arrow.hideturtle()
			arrowstate = "ready"
			arrow.setposition(-400, 0)

			# Reset the balloon
			x = random.randint(-100, 280)
			y = random.randint(-350, -300)
			balloon.setposition(x, y)

			# update the score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))



	# Move the Arrow 
	if arrowstate == "fire":
		x = arrow.xcor()
		x += arrowspeed
		arrow.setx(x)

	# check to see if the arrow has gone to the left-end
	if arrow.xcor() > 275:
		arrow.hideturtle()
		arrowstate = "ready"





# delay = input("press enter to finish")