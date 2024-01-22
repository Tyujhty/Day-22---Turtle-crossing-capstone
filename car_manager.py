from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_X_POSITION = 280
NUMBER_OF_CARS = 10

class Car(Turtle):
    all_cars = []
    def __init__(self, y_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(STARTING_X_POSITION, y_position)

    def create_car(self, number_of_cars):
        for _ in range(number_of_cars):
            y_position = random.randint(-280, 280)
            new_car = Car(y_position)
            self.all_cars.append(new_car)

    def car_move(self):
        self.forward(5)

    def increase_number_of_cars(self,number_of_cars):
        self.create_car(number_of_cars)

