from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
turtle = Player()

screen.listen()
screen.onkey(turtle.move, "Up")

while game_is_on:
    screen.update()

    # Detect when the player reaches the top of the screen
    if turtle.ycor() >= 290:
        game_is_on = False



screen.exitonclick()