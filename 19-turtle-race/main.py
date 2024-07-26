from turtle import *
from random import *

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet!", prompt="Wich turtle is the fastest? Chose a color between: red, "
                                                           "green, yellow, blue, orange and purple")
positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "green", "yellow", "blue", "orange", "purple"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.color()
            if user_bet == winner:
                print(f"You won! The winner is {winner}")
            else:
                print(f"You lost. The winner is {winner}")
        else:
            turtle.forward(randint(5, 20))


screen.exitonclick()
