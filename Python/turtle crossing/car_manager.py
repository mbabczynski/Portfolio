from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_INTERVAL = [1, 2, 1.5, 3]


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.chance = 6
    def create_cars(self):

        if random.randint(1, self.chance) == 1:
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.goto(280, random.randrange(-250, 250))
            #time.sleep(random.choice(CAR_INTERVAL))
            self.all_cars.append(car)
        for c in range(len(self.all_cars)):
            self.all_cars[c].forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
        if self.chance > 2:
            self.chance -= 1



