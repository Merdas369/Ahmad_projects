from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_snake = Snake()
food = Food()
scoreboard = ScoreBoard()
my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")
my_screen.tracer(0)
game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.get_score()
    for snake in my_snake.timy_group[1:]:
        if my_snake.head.distance(snake) < 1:
            game_on = False
            scoreboard.game_over()


    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280 :
        game_on = False
        scoreboard.game_over()



















my_screen.exitonclick()