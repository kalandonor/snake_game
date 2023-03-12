import time

from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

SIZE_OF_SCREEN = 620


class SnakeGame:
    def __init__(self):
        self.screen = self.init_screen()
        self.sam_the_snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.screen.onkeypress(self.sam_the_snake.up, "Up")
        self.screen.onkeypress(self.sam_the_snake.down, "Down")
        self.screen.onkeypress(self.sam_the_snake.left, "Left")
        self.screen.onkeypress(self.sam_the_snake.right, "Right")
        self.screen.listen()

    @staticmethod
    def init_screen():
        screen = Screen()
        screen.setup(width=SIZE_OF_SCREEN, height=SIZE_OF_SCREEN)
        screen.bgcolor("black")
        screen.title("My snake game")
        screen.tracer(0)
        screen.update()
        return screen

    def play(self):
        while not self.sam_the_snake.is_game_over():
            self.screen.update()
            time.sleep(0.1)
            self.sam_the_snake.move()
            if self.sam_the_snake.head.distance(self.food) < 15:
                self.food.refresh_food()
                self.scoreboard.increase_score()
                self.sam_the_snake.increase_size_of_snake()
        if self.sam_the_snake.is_game_over():
            self.scoreboard.save_high_score()
            self.scoreboard.game_over()
        self.screen.exitonclick()
