from turtle import Turtle
import random


def generate_random_coordinates():
    coordinates = [random.randint(-280, 280), random.randint(-280, 280)]
    return tuple(coordinates)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.goto(generate_random_coordinates())

    def refresh_food(self):
        self.goto(generate_random_coordinates())
