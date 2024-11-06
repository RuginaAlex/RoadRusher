import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = -10

LANE = [-195,-143,-93,-43,43,93,143,195]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        random_y = random.choice(LANE)


        # Creați mașina doar cu șansă de 1 la 6
        if random_chance == 1:
            if random_y < 0:
                new_car = Turtle("cars/right_truck.gif")
                new_car.penup()
                new_car.setheading(0)  # Să meargă spre dreapta
                new_car.goto(-430, random_y)
            else:
                new_car = Turtle("cars/truck.gif")
                new_car.penup()
                new_car.setheading(180)  # Să meargă spre stânga
                new_car.goto(430, random_y)

            new_car.shapesize(stretch_wid=1.5, stretch_len=3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)



    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT