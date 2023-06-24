from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_COUNT = 15

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.should_spew_cars = True
        self.move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT
        self.all_cars = []
        self.car_count = CAR_COUNT




    # Call this whenever the user levels up and we need to speed up the cars
    def increase_increment(self):
        self.move_distance += self.move_increment

    def spawn_car(self):
        if len(self.all_cars) < self.car_count:
            new_car = Turtle(shape="square")
            new_car.hideturtle()
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.goto(random.randint(300, 900), random.randint(-280, 280))
            new_car.showturtle()
            self.all_cars.append(new_car)



    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)
            if(car.xcor() < -300):
                print("car respawning")
                car.goto(random.randint(300, 600), random.randint(-280, 280))





