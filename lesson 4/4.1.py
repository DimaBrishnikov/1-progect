import random

class Human:
    def __init__(self, name, house=None, car=None, job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 100
        self.gladness = 50
        self.satiety = 50


brand_of_cars = {"BMW": {"fuel": 100, "strength": 100, "consumption":6},
            "Audi": {"fuel": 100, "strength": 100, "consumption": 6},
            "Mercedes": {"fuel": 80, "strength": 100, "consumption": 6},
            "Tesla": {"fuel": 50, "strength": 100, "consumption": 6}}

class Car:
    def __init__(self, brand_of_cars):
        self.brand = random.choice(list(brand_of_cars))
        self.fuel = brand_of_cars[self.brand]["fuel"]
        self.strength = brand_of_cars[self.brand]["strength"]
        self.consumption = brand_of_cars[self.brand]["consumption"]

    def drive(self):
        pass



class House:
    def __init__(self):
        self.food = 0
        self.mess = 0




job_list = {"Розробник на Python": {"salary": 100, "gladness_less": 10},
            "Кассир": {"salary": 20, "gladness_less": 50},
            "Викладач у школі МБУ СОШ": {"salary": 50, "gladness_less": 80},
            "Uber": {"salary": 40, "gladness_less": 20}}



class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]