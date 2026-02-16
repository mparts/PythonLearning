import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car_list = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.player_move, "Up")

speed = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(0,5) == 0:
        car = CarManager()
        car_list.append(car)
    for cars in car_list:
        if player.distance(cars) < 20:
            game_is_on = False
            score.game_over()
        cars.car_move(speed)
        if cars.xcor() < -310:
            del car_list[0]
            cars.hideturtle()

    if player.ycor() >= 280:
        score.level_up()
        player.homecoming()
        speed += 10

screen.exitonclick()
