from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def lose(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align="center", font=FONT)

    def win(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)
