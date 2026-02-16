import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -115
all_turtles = []

def turtle_create(color):
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(-200, y)
    all_turtles.append(tim)

for i in colors:
    turtle_create(color= i)
    y += 50
if user_bet:
    is_race_on =True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0, 10))
screen.exitonclick()