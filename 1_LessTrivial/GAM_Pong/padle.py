from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(starting_position)


    def up(self):
        ney_y = self.ycor() + 20
        self.goto(self.xcor(), y= ney_y)

    def down(self):
        ney_y = self.ycor() - 20
        self.goto(self.xcor(), y= ney_y)