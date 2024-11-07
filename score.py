from turtle import Turtle

class Score(Turtle):
    score = 0
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.color('white')
        self.write(("Score: " + str(self.score)), move = False, align="center", font=("Arial", 25, 'italic'))
    
    def update(self):
        self.clear()
        self.write(("Score: " + str(self.score)), move = False, align="center", font=("Arial", 25, 'italic'))