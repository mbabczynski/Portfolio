from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(230, 375)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Poprawne odpowiedzi: {self.score}/16", font=FONT, align=ALIGN)

    def add_score(self):
        self.score += 1
        self.update_score()