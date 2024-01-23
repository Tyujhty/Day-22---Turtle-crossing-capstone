from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(10)

    # Detect when the player reaches the top of the screen
    def reset_position(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
