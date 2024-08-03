from turtle import Turtle, Screen
from snake import Snake
import random
import time
from food import Food
from scoreboard import Scoreboard

# # Create screen
# screen = Screen()
# screen.setup(width=700, height=600)
# screen.listen()
# screen.bgcolor("black")
#
# snake = Turtle()
# snake.shape("square")
# snake.color("white")
# snake2 = Turtle()
# snake2.shape("square")
# snake2.color("white")
# snake3 = Turtle()
# snake3.shape("square")
# snake3.color("white")
#
# snake.penup()  # Lift the pen so it doesn't draw
# snake.goto(40, 0)  # Move to the desired starting position
# snake.pendown()
# snake2.penup()  # Lift the pen so it doesn't draw
# snake2.goto(20, 0)  # Move to the desired starting position
# snake2.pendown()
# snake3.penup()  # Lift the pen so it doesn't draw
# snake3.goto(0, 0)  # Move to the desired starting position
# snake3.pendown()
#
# food = Turtle()
# food.shape("circle")
# food.color("red")
#
#
# def food_pos():
#     food.penup()
#     food.goto(random.randint(-340, 340), random.randint(-290, 290))
#
#
# def forward():
#     snake.penup()
#     snake.forward(10)
#     snake2.penup()
#     snake2.forward(10)
#     snake3.penup()
#     snake3.forward(10)
#
#
# def backward():
#     snake.penup()
#     snake.backward(10)
#     snake2.penup()
#     snake2.backward(10)
#     snake3.penup()
#     snake3.backward(10)
#
#
# def move_clockwise():
#     snake.setheading(90)
#     snake.forward(10)
#     snake2.setheading(90)
#     snake2.forward(10)
#     snake3.setheading(90)
#     snake3.forward(10)
#
#
# def move_anticlockwise():
#     snake.setheading(270)
#     snake.forward(10)
#     snake2.setheading(270)
#     snake2.forward(10)
#     snake3.setheading(270)
#     snake3.forward(10)
#
#
# screen.onkey(key="w", fun=forward)
# screen.onkey(key="s", fun=backward)
# screen.onkey(key="a", fun=move_clockwise)
# screen.onkey(key="d", fun=move_anticlockwise)
#
#
# screen.onkey(key="b", fun=food_pos)
# screen.exitonclick()
#


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segments = []

# segment is an empty list in which each turtle object will be added automatically after the for loop

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
