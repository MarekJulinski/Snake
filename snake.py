from turtle import *


class Snake():
    
    size = 0.9
    shape = "square"
    color = "white"
    snake_len = 3
    new_snake_len = 3
    body = []
    start_pos = [(-5, -35), (-25, -35), (-45, -35)]
    
    
    def __init__(self) -> None:
        
        for i in range(len(self.start_pos)):
            part = SnakePart()
            self.body_init(part)
            part.goto(self.start_pos[i])

    def body_init(self, part):
        part.penup()
        part.shape(self.shape)
        part.shapesize(self.size, self.size)
        part.color(self.color)
        self.body.append(part)

    def check_border(self, head):
        coor = head.pos()
        is_head_in = True
        
        if coor[0] > 270 or coor[0] < -270:
            is_head_in = False
        
        if coor[1] > 240 or coor[1] < -270:
            is_head_in = False
            
        if is_head_in == False:
            self.clear()
            self.snake_over()
        
        return is_head_in
            
    def move(self):
        
        for i in range(self.snake_len-1, -1, -1):
            if i == 0:
                self.body[0].forward(20)
                can_move = self.check_border(self.body[0])
                
            else:
                self.body[i].goto(self.body[(i-1)].pos())
        
        self.snake_len = self.new_snake_len
        
        return can_move
            
    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)
    
    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)
    
    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)
    
    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)
    
    def clear(self):
        for segment in self.body:
            segment.reset()

    def snake_over(self):
        lost = Turtle()
        lost.hideturtle()
        lost.goto(0, 20)
        lost.penup()
        lost.color('red')
        lost.write("GAME OVER\nYOU LOST", move = False, align="center", font=("Arial", 25, 'italic'))
    
    def snake_extend(self):
        body = SnakePart()
        body.setpos(self.body[-1].pos())
        self.body_init(body)
    
    def check_collision(self):
        is_collided = False
        
        for i in range (1, len(self.body)):
            if self.body[0].distance(self.body[i]) < 9:
                self.clear()
                self.snake_over()
                is_collided = True
                
            if is_collided:
                break
        return is_collided
    
class SnakePart(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        