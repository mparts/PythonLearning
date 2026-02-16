from  turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(310, random.randint(-240, 280))
        self.shapesize(stretch_wid=1, stretch_len=2)

    def car_move(self, speed):
        self.forward(STARTING_MOVE_DISTANCE + speed)
