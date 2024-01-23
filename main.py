from turtle import Screen
from player import Player
from car_manager import Car

import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
turtle = Player()

car = Car()


screen.listen()
screen.onkey(turtle.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()

screen.exitonclick()