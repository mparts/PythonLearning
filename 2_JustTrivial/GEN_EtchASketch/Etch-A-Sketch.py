from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(5)
def move_backwards():
    tim.backward(5)
def turn_clockwise():
    tim.right(5)
def turn_counterclockwise():
    tim.left(5)
def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_counterclockwise)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()