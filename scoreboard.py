from turtle import Turtle, Screen

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-380, 180)
        self.write(f"Level: {self.level} ", False, "left", FONT)

        # This is the turtle for the Waiting Message at the beginning of the game
        self.wait_message = Turtle()
        self.wait_message.color("white")
        self.wait_message.hideturtle()
        self.wait_message.penup()


        # This is the turtle for the GO! message
        self.go_message = Turtle()
        self.go_message.color("yellow")
        self.go_message.hideturtle()
        self.go_message.penup()


    def update_score(self):
        self.clear()
        self.goto(-380, 180)
        self.write(f"Level: {self.level} ", False, "left", FONT)

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(-115, 10)
        self.color("red")
        self.write("GAME OVER", False, "left", ("Courier", 30, "bold"))

    def wait(self):
        self.wait_message.goto(-0, 10)
        self.wait_message.write("WAIT FOR THE", align="center", font=FONT)
        self.wait_message.goto(-0, -10)
        self.wait_message.write("HIGHWAY TO POPULATE", align="center", font=FONT)

    def clear_wait_message(self):
        self.wait_message.clear()

    def show_go_message(self):
        self.go_message.goto(0, 0)
        self.go_message.write("GO!", align="center", font=("Courier", 30, "bold"))

        Screen().ontimer(self.clear_go_message, 2000)

    def clear_go_message(self):
        self.go_message.clear()
