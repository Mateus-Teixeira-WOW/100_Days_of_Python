import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.up, "w")
screen.onkey(player.down, "s")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    # detect colisions
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            scoreboard.lose()
            screen.update()
            time.sleep(1.0)
            game_is_on = False

    # detect level victory
    if player.ycor() >= 250:
        car_manager.increase_speed()
        scoreboard.win()
        player.goto_start()
