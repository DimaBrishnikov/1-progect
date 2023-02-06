import random

class Student:
    def __init__(self,name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True
        self.money = 50




    def to_study(self):
        print("Я навчаюсь")
        self.progress += 0.2
        self.gladness -= 5


    def to_sleep(self):
        print("Я пішов спати")
        self.gladness += 3


    def to_have_fun(self):
        print("Я пішов розважатися")
        self.progress -= 0.1
        self.gladness += 6
        self.money -= 4




    def to_work(self):
        print("Я працюю.")
        self.gladness -= 5
        self.money += 5





    def is_alive(self):
        if self.progress <0:
            print("Вас відраховано від навчального закладу")
            self.alive = False
        if self.progress >5:
            print("Я достроково завершив МКА")
            self.alive = False
        elif self.progress < 1:
            self.to_study()
        if self.gladness < 0:
            print("Все пропало. В мене депрессія")
            self.alive = False
        if self.money < 20:
            self.to_work()


    def end_of_day(self):
        print(f"Задоволеньсть - {self.gladness}")
        print(f"Прогрес - {round(self.progress , 2)}")
        print(f'Мої кошити - {self.money}.')

    def live(self, day):
        info = f"День{day}: з життя {self.name}"
        print(f"{info:=^40}")
        choice = random.randint (1, 3)
        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.to_have_fun()
        elif choice == 4:
            self.to_work()
        elif self.progress < 0.2:
            self.to_study
        elif self.gladness < 10:
            self.to_have_fun()
        elif self.money < 10:
            self.to_work()

        self.end_of_day()
        self.is_alive()



dmytro = Student(name="Дмитро")
for day in range(365):
    if dmytro.alive == False:
        break
    dmytro.live(day)