from turtle import Screen
from padle import Paddle
from ball import Ball
from scoreboard import Scoreboard 
from boundaries import Boundaries
import time

def back_to_menu():
    score.update_highscore()
    return screen.bye

screen = Screen()
screen.bgcolor("black")
screen.setup(1000, 900)
screen.title("Pong")
screen.tracer(0)

boundaries = Boundaries()
player1 = Paddle((-350, 0))
player2 = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(player1.up, "w"), screen.onkey(player1.up, "W")
screen.onkey(player1.down, "s"), screen.onkey(player1.down, "S")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")
screen.onkey(back_to_menu(), "q"), screen.onkey(back_to_menu(), "Q")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() >= 330 and ball.distance(player2) < 50 or ball.xcor() <= -330 and ball.distance(player1) < 50:
        ball.bounce_x()
    elif ball.xcor() > 400:
        ball.reset_pos()
        score.p1_point()
    elif ball.xcor() < -400:
        ball.reset_pos()
        score.p2_point()