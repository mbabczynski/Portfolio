from turtle import Turtle
import random
DIRECTION = random.choice([random.randint(225, 315), random.randint(45, 135)])

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.setheading(DIRECTION)

    def ball_move(self):
        self.forward(1)

    def collision(self):
        x= self.heading()
        if 0 <= x < 90:
            self.setheading(180-x)
        if 90 <= x < 180:
            self.setheading(180-x)
        if 180 <= x < 270:
            self.setheading(360 - (x-180))
        if 270 <= x < 360:
            self.setheading((360-x)+180)

    def paddle_collision(self):
        x= self.heading()
        if 0 <= x < 90:
            self.setheading(270 + (x % 90))
        if 90 <= x < 180:
            self.setheading(270 - (x % 90))
        if 180 <= x < 270:
            self.setheading(90 + (x % 90))
        if 270 <= x < 360:
            self.setheading(90 - (x % 90))

    def new_round(self):
        self.setheading(random.choice([random.randint(225, 315), random.randint(45, 135)]))
        self.goto(0, 0)

