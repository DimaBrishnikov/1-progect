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




    def eat(self):
        pass



    def work(self):
        pass


    def shopping(self, purchase):
        pass


    def cleaning(self):
        pass


    def to_repair(self):
        pass


    def chill(self):
        pass

    def get_house(self):
        self.house = House()



    def get_car(self):
        self.car = Car(brand_of_cars)



    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)



    def is_alive(self):
        if self.gladness <0:
            print("Депресія...")
            return False
        if self.satiety <0:
            print("Помер від голоду")
        if self.money < -200:
            print("Банкрот.....")
            return False


    def day_info(self, day_number):
        day_str = f" День {day_number} й з життя {self.name}а"
        print(f"{day_str:=^50}", "\n")
        human_str = f"Інформація {self.name}а"
        print(f"{human_str:=^50}", "\n")
        print(f"Задоволення - {self.gladness}")
        print(f" Ситість  - {self.satiety}")
        print(f" Грощі  - {self.money}")
        house_str = f"Інформація про будинок"
        print(f"{house_str:=^50}", "\n")
        print(f"Іжа - {self.house.food}")
        print(f"Порядок - {self.house.mess}")
        car_str = f"Інформація про автівку {self.car.brand}"
        print(f"{car_str:=^50}", "\n")
        print(f"Пальне- {self.car.fuel}")
        print(f"Стан - {self.car.strength}")


    def live(self, day_number):
        if self.is_alive() == False:
            return False
        if self.house is None:
            self.get_house()
            print("Поселилися в будинку")
        if self.car is None:
            self.get_car()
            print(f"Прибав автівку {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Влаштувався на работу {self.job.job}, із зарплатнею {self.job.salary}$")
        self.day_info(day_number)




brand_of_cars = {"BMW": {"fuel": 100, "strength": 100, "consumption": 6},
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
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= 1
            self.strength -= 1
            return True
        else:
            print("Немае пального або авто зламалось")
            return False


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



dmytro = Human("Дмитр")
for day in range(1,366):
    if dmytro.live(day) == False:
        break