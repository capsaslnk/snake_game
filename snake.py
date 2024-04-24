from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Create the starting snake"""

    def __init__(self):
        """Initializing of snake class and creating of the snake"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Method for creating the snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Method adding segments to snake"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Method for extending the snake tail"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moving of the snake forward continuously"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Change the snake heading by 90deg"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake heading by 270deg"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake heading by 180deg"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake heading by 0deg"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
