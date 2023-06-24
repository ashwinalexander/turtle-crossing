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
car_manager = CarManager()


screen.tracer(0)

screen.listen()
screen.onkey(lil_turtle.move_forward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if len(car_manager.all_cars) < car_manager.car_count:
        print("spawning car")
        car_manager.spawn_car()
    car_manager.move_cars()
    screen.update()


    # the turtle has made it to the end, start a new level
    if lil_turtle.ycor() >= lil_turtle.finish_line:
        lil_turtle.reset_turtle()
        scoreboard.increment_level()
