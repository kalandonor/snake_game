from turtle import Turtle
import os


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = self.get_high_score()
        self.score = 0
        self.goto((-25, 290))
        self.penup()
        self.shape("square")
        self.fillcolor("black")
        self.pencolor("orange")
        self.hideturtle()
        self.update_score_board()

    @staticmethod
    def get_high_score():
        path = './high_score.txt'
        if os.path.isfile(path):
            with open(path, 'r') as hs:
                return int(hs.read().strip())
        return 0

    def update_score_board(self):
        self.clear()
        self.write(f"Score is {self.score}, high score: {self.high_score}")

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over! Your score is {self.score}", align="center", font=('Arial', 16, "normal"))

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as hs:
                hs.write(f"{self.high_score}")
