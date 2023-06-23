import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
lil_turtle = Player()
screen.title("Turtle Crossing")
scoreboard = Scoreboard()


screen.tracer(0)

screen.listen()
screen.onkey(lil_turtle.move_forward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if lil_turtle.ycor() >= lil_turtle.finish_line:
        lil_turtle.reset_turtle()
        scoreboard.increment_level()
