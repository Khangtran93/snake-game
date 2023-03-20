from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Score
import time

screen = Screen()

color = ["red","blue","green","brown","gray","purple","pink","turquoise","yellow","white","orange"]

SCREEN_WIDTH = 600
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor('black')
screen.tracer(0)

border = Turtle()
border.hideturtle()
border.shape("turtle")
border.color("white")
border.speed(5)
border.penup()
border.goto(-270, -270)
border.showturtle()
border.pendown()
border.forward(540)
border.left(90)
border.forward(540)
border.left(90)
border.forward(540)
border.left(90)
border.forward(540)
border.hideturtle()


#screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.to_og, "g")
#screen.onkey(score.reset_game, "r")

game_is_on = True
#speed = 0.1
while game_is_on:
    screen.update()
    if snake.speed < 0:
        snake.speed = 0.1
    time.sleep(snake.speed)

    snake.move()

    if snake.head.distance(food) < 20:
        food_color = food.color()[0]
        print(food_color)
        food.refresh()
        snake.extend(food_color)

        score.increase_score()
        snake.increase_speed()
        #snake.speed = snake.speed - score.score/10

    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        #print("triggered at collision with wall")
        #again = screen.textinput(title="Game over.", prompt="Want to try again? ")
        #if again == 'y':
        #screen.clear()
        score.reset()
        snake.reset()




        #else:
        #    #game_is_on = False
        #    score.game_over()
        #    break

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            print(snake.head.distance(segment))
            print("trigger at collision with tails")
            print(snake.head.position())
            print(segment.position())
            #game_is_on = False
            score.game_over()


















screen.exitonclick()