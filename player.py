import random
from turtle import Turtle


STARTING_POSITION = (0, -223)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280
DEATH = ["walker_graph/dead1.gif","walker_graph/dead2.gif"]

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("walker_graphic.gif")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.level_up()



    def up(self):
        # This is just for the first move to be in te middle of the first lane
        if self.ycor() == -223:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)


        # This modifies the jump to ensure the player lands in the center of the middle-grass lane
        elif self.ycor() == -43:
            new_y = self.ycor() + 42
            self.goto(self.xcor(), new_y)

        elif self.ycor() == -1:

            new_y = self.ycor() + 42
            self.goto(self.xcor(), new_y)


        elif self.ycor() == 191:
            new_y = self.ycor() + 39
            self.goto(self.xcor(), new_y)

        else:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(),new_y)

    def down(self):

        if self.ycor() > -223:
            if self.ycor() == -193:
                new_y = self.ycor() - 30
                self.goto(self.xcor(), new_y)

            elif self.ycor() == -1:
                new_y = self.ycor() - 42
                self.goto(self.xcor(), new_y)

            elif self.ycor() == 41:
                new_y = self.ycor() - 42
                self.goto(self.xcor(), new_y)

            elif self.ycor() == 230:
                new_y = self.ycor() - 39
                self.goto(self.xcor(), new_y)

            else:
                new_y = self.ycor() - MOVE_DISTANCE
                self.goto(self.xcor(), new_y)

    def level_up(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.shape(random.choice(DEATH))
