from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.write(f"{self.p1_score}|{self.p2_score} ", align="center", font=("Courier", 50, 'normal'))

    def update_score_p1(self):
        self.clear()
        self.p1_score += 1
        self.write(f"{self.p1_score}|{self.p2_score} ", align="center", font=("Courier", 50, 'normal'))

    def update_score_p2(self):
        self.clear()
        self.p2_score += 1
        self.write(f"{self.p1_score}|{self.p2_score} ", align="center", font=("Courier", 50, 'normal'))
