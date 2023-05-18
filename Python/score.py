from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.goto(0, 195)
        self.print_score()


    def add_left(self):
        self.score_left += 1
        self.print_score()


    def add_right(self):
        self.score_right += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.score_left} : {self.score_right}", align="center", font=("Courier", 40, "bold"))



