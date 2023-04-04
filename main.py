import turtle
import time
from snack import Snake
from food import Food
from score import Score


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("lomaa")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"8")
screen.onkey(snake.down,"5")
screen.onkey(snake.left,"4")
screen.onkey(snake.right,"6")
screen.onkey(snake.north_west,"7")
screen.onkey(snake.south_west,"1")
screen.onkey(snake.south_East,"3")
screen.onkey(snake.north_East,"9")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.10)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_ali()
        score.score_incress()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    for ali in snake.ali_list[1:]:

        if snake.head.distance(ali) < 5:
            game_is_on = False
            score.game_over()



screen.exitonclick()

