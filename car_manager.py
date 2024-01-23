from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_X_POSITION = 280
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.25


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Random chance of creating a new car
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            new_car.goto(STARTING_X_POSITION, y_position)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increase_speed(self):
        for car in self.all_cars:
            self.move_speed += MOVE_INCREMENT
