from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,250)
        self.score = 0
        with open("data.txt") as file:
            self.highScore = int(file.read())
        self.displayScore()

    def displayScore(self):
        self.clear()
        self.write(f"Score: {self.score} High score : {self.highScore}", align=ALIGNMENT,  font=FONT)
        self.hideturtle()

    def increaseScore(self):
        self.score += 1

    def reset(self):
        if self.score > self.highScore :
            self.highScore = self.score
            with open("data.txt") as file:
                file.write(f"{self.highScore}")
        self.score = 0
        self.displayScore()