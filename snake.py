import turtle
from turtle import Turtle

HALF_SIZE = 295
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


def initialize_snake_body():
    turtle.mode("standard")
    snake_body = []
    for position in STARTING_POSITION:
        snake_body.append(add_body_part(position))
    return snake_body


def add_body_part(position):
    body_part = Turtle()
    body_part.shape("square")
    body_part.color("white")
    body_part.penup()
    body_part.goto(position)
    return body_part


class Snake:
    def __init__(self):
        self.snake_body = initialize_snake_body()
        self.head = self.snake_body[0]

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].pos())
        self.head.forward(DISTANCE)

    def is_game_over(self):
        is_game_over = False
        if self.head.xcor() > HALF_SIZE or self.head.xcor() < \
                HALF_SIZE * -1 or self.head.ycor() > \
                HALF_SIZE or self.head.ycor() < HALF_SIZE * -1 or self.is_body_collision_happened():
            is_game_over = True
        return is_game_over

    def up(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(0)

    def get_snake_body_part_coordinates_without_head(self):
        return [body_part.pos() for body_part in self.snake_body[1:]]

    def is_body_collision_happened(self):
        snake_body_part_coordinates = self.get_snake_body_part_coordinates_without_head()
        body_collision_list = [self.head.distance(body_part_coordinate) < 15
                               for body_part_coordinate in snake_body_part_coordinates]
        return any(body_collision_list)

    def increase_size_of_snake(self):
        new_body_part = add_body_part(self.snake_body[-1].pos())
        self.move()
        self.snake_body.append(new_body_part)

    def hide_snake(self):
        for body_part in self.snake_body:
            body_part.hideturtle()
            body_part.goto(1000, 1000)

    def reset_snake(self):
        self.hide_snake()
        self.snake_body.clear()
        self.snake_body = initialize_snake_body()
        self.head = self.snake_body[0]

