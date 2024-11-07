from turtle import *
from snake import *
from score import Score
from food import Food
import time
import os

DIR = os.path.dirname(os.path.realpath(__file__))

def create_screen():
    screen = Screen()
    screen.setup(548, 548)
    screen.tracer(0)
    screen.bgcolor('black')
    return screen

def create_border():
    border = Turtle()
    border.hideturtle()
    border.penup()
    border.goto(-270, 236)
    border.pendown()
    border.color("white")
    border.goto(270, 236)

if __name__ == "__main__":
    
    screen = create_screen()
    snake = Snake()
    score = Score()
    food = Food()
    
    
    
    with open(str(DIR) + '/highscore.txt', "r") as f:
        highscore = f.readline()
        
    h_score = Turtle()
    h_score.hideturtle()
    h_score.penup()
    h_score.setpos(200, 245)
    h_score.color('white')
    h_score.write(("High Score: " + highscore), move = False, align="center", font=("Arial", 10, 'italic'))
    
    create_border()
    
    screen.update()
    
    screen.onkeypress(snake.right, "d")
    screen.onkeypress(snake.left, "a")
    screen.onkeypress(snake.up, "w")
    screen.onkeypress(snake.down, "s")
    screen.listen()
    
    game = True
    
    time.sleep(1)
    
    while game:
        time.sleep(0.1)
        
        game = snake.move()
        
        food.is_eaten(snake, score)
        
        game = not(snake.check_collision())
        
        if score.score >= 663:
            game = False
        
        screen.update()
    
    food.reset()
    
    if score.score > int(highscore):
        highscore = str(score.score)
        with open(str(DIR) + '/highscore.txt', "w") as f:
            f.write(highscore)
            f.close()
    
    screen.update()
    screen.exitonclick()