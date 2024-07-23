import colorgram
import random
from turtle import *

t = Turtle()
t.pensize(20)
screen = Screen()
screen.colormode(255)
t.speed("fastest")
t.hideturtle()


# colors = colorgram.extract("hirst_painting.jpeg", 20)
#
# list_rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     list_rgb.append(new_color)
# print(list_rgb)

COLORS = [(251, 249, 245), (209, 165, 124), (249, 234, 236), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (215, 234, 231), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190)]


def draw_painting():
    global COLORS

    def go_to_start_position():
        t.up()
        t.goto(-150, -100)

    def make_one_line():
        for _ in range(5):
            t.down()
            t.forward(1)
            t.up()
            t.forward(50)
            t.down()
            t.forward(1)
            t.up()

    def turn_left():
        t.left(90)
        t.forward(50)
        t.left(90)

    def turn_right():
        t.right(90)
        t.forward(50)
        t.right(90)

    go_to_start_position()
    turtle_color = random.choice(COLORS)
    t.color(turtle_color)
    make_one_line()
    turn_left()
    turtle_color = random.choice(COLORS)
    t.color(turtle_color)
    make_one_line()
    turtle_color = random.choice(COLORS)
    t.color(turtle_color)
    turn_right()
    make_one_line()
    turtle_color = random.choice(COLORS)
    t.color(turtle_color)
    turn_left()
    make_one_line()
    turtle_color = random.choice(COLORS)
    t.color(turtle_color)
    turn_right()
    make_one_line()
    turtle_color = random.choice(COLORS)
    t.color(turtle_color)
    turn_left()
    make_one_line()
    turtle_color = random.choice(COLORS)
    t.color(turtle_color)


draw_painting()

screen.exitonclick()
