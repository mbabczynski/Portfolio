from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def add_score(self):
        self.level += 1
        self.print_score()

    def game_over(self):
        self.goto(-80, 0)
        self.write("GAME OVER", font=FONT)