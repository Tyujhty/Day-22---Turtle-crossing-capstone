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

number_of_cars = 5
y_position = random.randint(-280, 280)

car = Car(y_position)
car.create_car(number_of_cars)

screen.listen()
screen.onkey(turtle.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    turtle.reset_position(number_of_cars)


screen.exitonclick()