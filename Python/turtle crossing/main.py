import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
level = Scoreboard()
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkeypress(player.move, "Up")
    car.create_cars()
    if player.ycor() >= 280:
        player.next_turn()
        level.add_score()
        car.speed_up()
    for c in car.all_cars:
        if player.distance(c) < 20:
            game_is_on = False

level.game_over()
screen.exitonclick()
