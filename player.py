from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset_turtle()
        self.color("black")
        self.finish_line = FINISH_LINE_Y

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)