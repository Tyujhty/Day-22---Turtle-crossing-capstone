from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

game_is_on = True
turtle = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()


    # Detect when turtle reaches top
    if turtle.ycor() > 280:
        turtle.reset_position()
        car_manager.increase_speed()
        scoreboard.update_score()

screen.exitonclick()