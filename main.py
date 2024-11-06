import time
from turtle import Screen

from background import create_world
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.title("Cross the Road")
screen.register_shape("walker_graphic.gif")
screen.register_shape("cars/truck.gif")
screen.register_shape("cars/right_truck.gif")
screen.register_shape("walker_graph/dead1.gif")
screen.register_shape("walker_graph/dead2.gif")
screen.setup(height=480, width=800)
screen.tracer(0)


create_world()
alex = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()




game_is_on = True
player_can_move = False

while game_is_on:
    increment = 0
    time.sleep(0.1)
    screen.update()

    if not player_can_move:
        score.wait()

    if not player_can_move and len(car_manager.all_cars) >= 10:
        score.clear_wait_message()
        score.show_go_message()
        screen.onkeypress(alex.up, "Up")
        screen.onkeypress(alex.down, "Down")
        player_can_move = True




    # Detects if the car hits the turtle

    for car in car_manager.all_cars:

        if abs(alex.ycor() - car.ycor()) < 20:
            # Definim limitele stânga și dreapta ale mașinii pe axa X
            car_left_edge = car.xcor() - 45
            car_right_edge = car.xcor() + 45

            # Check if the player is aligned with the car on the X axis
            if car_left_edge < alex.xcor() < car_right_edge:
                alex.game_over()
                score.game_over()
                screen.update()
                game_is_on = False
                break


    # Detects if you level up

    if alex.ycor() >= 270:
        alex.level_up()
        screen.update()
        score.level_up()
        car_manager.level_up()

    car_manager.create_car()
    car_manager.move_cars()


screen.exitonclick()