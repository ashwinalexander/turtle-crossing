from turtle import Turtle

FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # scoreboard housekeeping
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.update_score()

    def increment_level(self):
        self.level +=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)
