from turtle import *
import random

class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shape('circle')
        self.color('red')
        self.shapesize(0.5)
        self.find_position()
              
    def find_position(self):
        pos_x = random.randrange(-265, 255, 20)
        pos_y = random.randrange(-255, 225, 20)
        self.setpos(pos_x, pos_y)
        
    def is_eaten(self, snake, score):
        
        if self.distance(snake.body[0]) < 9:
            snake.snake_extend()
            score.update()
            snake.new_snake_len += 1
            score.score += 1
            score.update()
            self.find_position()
            for segment in snake.body:
                if self.distance(segment) < 9:
                    self.find_position()