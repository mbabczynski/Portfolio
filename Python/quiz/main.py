from turtle import Screen
from states import State
from score import Score

screen = Screen()
screen.setup(width=900, height=847)
screen.bgpic("poland_900x847.gif")
screen.title("QUIZ GEOGRAFICZNY")
state = State()
score = Score()

game_on = True

while game_on:
    answer = screen.textinput(title="Wiesz czy nie wiesz?", prompt="Wpisz nazwę województwa...")
    if answer is None:
        game_on = False
        continue
    answer = answer.lower()
    answer = answer.capitalize()
    if state.check_answer(answer):
        state.create_state(answer)
        score.add_score()

    if len(state.old_answers) == 16:
        state.print_message("Gratulacje!!!", size=32)
        game_on = False

screen.exitonclick()
