from turtle import Turtle

class Boundaries(Turtle):

    def __init__(self):
        super().__init__()
        self.left_, self.right_, self.bottom_, self.top_ = -400, 400, -300, 300
        self.color("white")
        self.penup()
        self.hideturtle()
        self.field_boundaries()
        self.score_board_separator()
        self.versus()

    def field_boundaries(self):
        self.pensize(3)
        self.penup()
        self.goto(0, self.bottom_)
        self.pendown()
        self.goto(0, -50)
        self.circle(50)
        self.penup()
        self.goto(0, 50)
        self.pendown()
        self.goto(0, self.top_)
        self.penup()
        self.goto(self.left_, self.bottom_)
        self.pendown()
        self.goto(self.left_, self.top_)
        self.goto(self.right_, self.top_)
        self.goto(self.right_, self.bottom_)
        self.goto(self.left_, self.bottom_)        

    def score_board_separator(self):
        self.pensize(6)
        self.penup()
        self.goto(-30, 360)
        self.pendown()
        self.goto(30, 360)

    def versus(self):
        self.penup()
        self.goto(0, -410)
        self.write("vs", align="center", font=("Courier", 20, "normal"))
        self.goto(-200, -410)
        self.write("Player1", align="center", font=("Courier", 20, "normal"))
        self.goto(200, -410)
        self.write("Player2", align="center", font=("Courier", 20, "normal")) 