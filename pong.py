#!/usr/bin/python

import turtle
import winsound

window = turtle.Screen()
window.title('Ping pong by @Jerwin')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#player 1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("white")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350,0)

#player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("white")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0
ball.dy = 0

#Score
score_player1 = 0
score_player2 = 0

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1 : {}   Player 2 : {}".format(score_player1, score_player2), align = "center", font = ("Courier", 24, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,200)
pen2.write("Press 1 to start.", align = "center", font = ("Courier", 15, "normal"))

#Move player 1
def player1_up():
	y = player_1.ycor()
	y += 20
	player_1.sety(y)

def player1_down():
	y = player_1.ycor()
	y -= 20
	player_1.sety(y)

#Move player 2
def player2_up():
	y = player_2.ycor()
	y += 20
	player_2.sety(y)

def player2_down():
	y = player_2.ycor()
	y -= 20
	player_2.sety(y)

def start_again():
	pen2.clear()
	ball.dx = 0.4
	ball.dy = 0.2


#Keyboard binding
window.listen()
#binding for player 1
window.onkeypress(player1_up,"w")
window.onkeypress(player1_down,"s")
#binding for player 2
window.onkeypress(player2_up,"Up")
window.onkeypress(player2_down,"Down")
window.onkeypress(start_again,"1")


#Main game loop
while True:
	window.update()

	#Move the ball
	ball.setx(ball.xcor() + ball.dx) #adding the current x-position of the ball with the value of ball.dx
	ball.sety(ball.ycor() + ball.dy) #adding the current x-position of the ball with the value of ball.dy

	#border checking
	if ball.ycor()>290: #check for border top
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		ball.sety(290)
		ball.dy *= -1 #setting the ball.dy to negative and it will reverse the direction of the ball go down

	elif ball.ycor()<-290: #check for border bottom
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		ball.sety(-290)
		ball.dy *= -1 #setting the ball.dy to positive and it will reverse the direction of the ball going up
	
	elif ball.xcor() > 390: #check for border right
		score_player1 += 1
		pen.clear()
		pen.write("Player 1 : {}   Player 2 : {}".format(score_player1, score_player2), align = "center", font = ("Courier", 24, "normal"))
		ball.goto(0,0) #making the ball back to original position
		ball.dx = 0
		ball.dy = 0
		player_1.goto(-350,0)
		player_2.goto(350,0)
		pen2.write("Press 1 to start again.", align = "center", font = ("Courier", 15, "normal"))

	elif ball.xcor() < -390: #check for border left
		score_player2 += 1
		pen.clear()
		pen.write("Player 1 : {}   Player 2 : {}".format(score_player1, score_player2), align = "center", font = ("Courier", 24, "normal"))
		ball.goto(0,0)
		ball.dx = 0
		ball.dy = 0
		player_1.goto(-350,0)
		player_2.goto(350,0)
		pen2.write("Press 1 to start again.", align = "center", font = ("Courier", 15, "normal"))

	elif (ball.xcor() < -340 and ball.xcor()>-350) and ((ball.ycor() < player_1.ycor() + 40) and (ball.ycor() > player_1.ycor() - 40)): #check for collision in player 1 and ball
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		ball.dx *= -1

	elif (ball.xcor() > 340 and ball.xcor()<350) and ((ball.ycor() < player_2.ycor() + 40) and (ball.ycor() > player_2.ycor() - 40)): #check for collision in player 2 and ball
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		ball.dx *= -1	

	elif (player_1.ycor() > 250): #make player 1 not go beyond the top border
		player_1.sety(250)

	elif (player_1.ycor() < -250): #make player 1 not go beyond the below border
		player_1.sety(-250)		

	elif (player_2.ycor() > 250): #make player 2 not go beyond the top border
		player_2.sety(250)

	elif (player_2.ycor() < -250): #make player 2 not go beyond the below border
		player_2.sety(-250)