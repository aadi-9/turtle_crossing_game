from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.update()

    def update(self):
        self.goto(-250, 250)
        self.write(f"Score: {self.score1}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def score_inc(self):
        self.score1 += 1
        self.clear()
        self.update()
