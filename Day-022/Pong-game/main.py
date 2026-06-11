# from turtle import Turtle, Screen
# from paddle import Paddle
# import time
# from ball import Ball
# from scoreboard import Scoreboard


# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("pong")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()
# scoreboard = Scoreboard
# scoreboard()

# screen.listen()
# screen.onkey(r_paddle.move_up, "Up")
# screen.onkey(r_paddle.move_down, "Down")
# screen.onkey(l_paddle.move_up, "w")
# screen.onkey(l_paddle.move_down, "s")




# game_is_on = True
# while game_is_on:
#     time.sleep(ball.move_speed)
#     screen.update()
#     ball.move()
#     #Detect collision with wall
#     if(
#          ball.ycor() > 280 
#          or ball.ycor() < -280
      
#     ):
#         ball.bounce_y()
#     #Detect collision with  paddle
#     if (
#          ball.distance(r_paddle) < 50 and ball.xcor() > 320 
#          or ball.distance(l_paddle) < 50  and ball.xcor() < -320
#      ):
        
#          ball.bounce_x()

#     #Detect if ball goes out r_paddle
#     if ball.xcor() > 380  :
#         ball.reset_position()
#         scoreboard.l_point()
    
#     if ball.xcor() < -380:
#         ball.reset_position()
#         scoreboard.r_point()


# screen.exitonclick()


















from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Keyboard controls
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)

    screen.update()

    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Right paddle collision
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
    ):
        ball.bounce_x()

    # Left paddle collision
    if (
        ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Right wall miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left wall miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()









