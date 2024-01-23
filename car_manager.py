from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_X_POSITION = 280
NUMBER_OF_CARS = 10


class Car():

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        y_position = random.randint(-250, 250)
        new_car.setheading(180)
        new_car.goto(STARTING_X_POSITION, y_position)
        self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(5)