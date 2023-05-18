from turtle import Turtle
import pandas
import time
ALIGN = "center"


class State:
    def __init__(self):
        self.data = pandas.read_csv("poland_data.csv")
        self.old_answers = []
        self.states = self.data["state"].tolist()

    def create_state(self, name):
        new_state = Turtle()
        new_state.color("black")
        new_state.penup()
        new_state.hideturtle()
        x = float(self.data[self.data["state"] == name]["x"])
        y = float(self.data[self.data["state"] == name]["y"])
        new_state.goto(x, y)
        new_state.write(name, align=ALIGN, font=("Courier", 20, "bold"))

    def check_answer(self, answer):
        if answer in self.states and answer not in self.old_answers:
            self.old_answers.append(answer)
            return True
        if answer in self.old_answers:
            self.print_message("Ta odpowiedź już padła wcześniej,\n spróbuj ponownie...", size=20)
            return False
        if answer not in self.states:
            self.print_message("Podaj poprawną nazwę,\n nazwy dwuczłonowe rodziel myślnikiem...", size=20)
            return False

    def print_message(self, message,size):
        backg = Turtle("square")
        backg.hideturtle()
        backg.color("white")
        backg.penup()
        backg.shapesize(stretch_len=36, stretch_wid=6)
        backg.goto(0, 180)
        backg.showturtle()
        new_message = Turtle()
        new_message.penup()
        new_message.hideturtle()
        new_message.goto(0, 150)
        new_message.write(message, align=ALIGN, font=("Courier", size, "bold"))
        time.sleep(3)
        new_message.clear()
        backg.hideturtle()


