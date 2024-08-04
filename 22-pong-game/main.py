from turtle import Screen
from paddle import Paddle, PLAYER_1_POSITION, PLAYER_2_POSITION
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
player1 = Paddle()
player2 = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "i")
screen.onkey(player2.down, "k")

player1.goto(PLAYER_1_POSITION)
player2.goto(PLAYER_2_POSITION)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # detect colisions between ball and walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect colision between ball and paddle
    if ball.distance(player1) < 50 and ball.xcor() < -320 or ball.distance(player2) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    # detect when p1 misses a ball
    if ball.xcor() < -360:
        ball.restart()
        ball.bounce_x()
        scoreboard.update_score_p2()
    # detect when p2 misses a ball
    if ball.xcor() > 360:
        ball.restart()
        ball.bounce_x()
        scoreboard.update_score_p1()
screen.exitonclick()
