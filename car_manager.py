from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        generate = random.randint(1,8)
        if generate == 1:
            new = Turtle("square")
            new.penup()
            new.goto(310, random.randint(-250,250))
            new.color(random.choice(COLORS))
            new.shapesize(1, 2)
            new.setheading(180)
            self.all_cars.append(new)

    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def inc_speed(self):
        self.speed += MOVE_INCREMENT


