from turtle import Turtle

FONT = ('Arial', 20, 'normal')
ALIGNMENT = "center"
MOVE = False


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 250)
        self.color("white")
        self.write(f"Score: {self.score} ", False, ALIGNMENT, FONT)
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", False, ALIGNMENT, FONT)

    def gameover(self):
        self.goto(0, 00)
        self.color("white")
        self.write("Game Over.", False, ALIGNMENT, FONT)