import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

leo = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(leo.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for cars in car.all_cars:
        if cars.distance(leo) < 20:
            game_is_on = False
            score.game_over()

    if leo.has_finish():
        leo.goto_start()
        car.inc_speed()
        score.score_inc()


screen.exitonclick()
