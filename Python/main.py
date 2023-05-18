import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score



screen = Screen()
screen.setup(width=1000, height=500)
screen.bgpic("image.gif")
screen.title("PONG")
screen.listen()
screen.mode(mode="logo")
screen.tracer(0)
score = Score()

paddle_left = Paddle(-450)
paddle_right = Paddle(450)
ball = Ball()


screen.onkeypress(paddle_left.move_up, key="w")
screen.onkeypress(paddle_left.move_down, key="s")
screen.onkeypress(paddle_right.move_up, key="Up")
screen.onkeypress(paddle_right.move_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    screen.update()
    ball.ball_move()
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.collision()
    if paddle_left.xcor() - 12 <= ball.xcor() <= paddle_left.xcor() + 12 \
            and paddle_left.ycor() - 45 <= ball.ycor() <= paddle_left.ycor() + 45:
        ball.paddle_collision()
    if paddle_right.xcor() - 12 <= ball.xcor() <= paddle_right.xcor() + 12 \
            and paddle_right.ycor() - 45 <= ball.ycor() <= paddle_right.ycor() + 45:
        ball.paddle_collision()
    if ball.xcor() > 480:
        score.add_left()
        ball.new_round()
    if ball.xcor() < -480:
        score.add_right()
        ball.new_round()



screen.exitonclick()