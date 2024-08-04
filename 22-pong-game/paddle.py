from turtle import Turtle

PLAYER_1_POSITION = (-350, 0)
PLAYER_2_POSITION = (350, 0)
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)
