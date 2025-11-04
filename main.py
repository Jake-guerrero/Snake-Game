from turtle import Screen, Turtle
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

Snake = Snake()
Food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    Snake.move()

    if Snake.head.distance(Food) < 15:
        Food.refresh()
        Snake.extend()
        Snake.extend()
        scoreboard.score_up()

    if Snake.head.xcor() > 280 or Snake.head.xcor() < -280 or Snake.head.ycor() > 280 or Snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.the_game_is_over()

    for segment in Snake.segments[1:]:
        if Snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.the_game_is_over()


screen.exitonclick()