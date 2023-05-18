from turtle import Turtle
POSITIONS = [-450, 450]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode(rmode="user")
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.penup()
        self.setx(position)

    def move_up(self):
        if self.ycor() < 230:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def move_down(self):
        if self.ycor() > -230:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)




