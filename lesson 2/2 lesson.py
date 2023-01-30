class Student:
    count_of_Student = 0
    def __init__(self, name=None,height=160,metal_ability=10.0):
        self.name = name
        self.height = height
        self.mental_ability = metal_ability
        Student.count_of_Student += 1
        print("Привіт я з,явился")

    def grow2(self, mental_ability=0.5):
        self.mental_ability += mental_ability
        print("Я підвищів свій рівень знань")

    def grow(self, height=1):
        self.height += height

    def __str__(self):
        return f"Я {self.name}, мій зріст {self.height} см мій розуковій праа {self.Mental_ability}"

    def __del__(self):
        print(f"Я {self.name}, і я пішов((")

Serg = Student(name="Serg",height=180)
print(Serg)
print(Serg.height)
print(Serg.name)
Serg.grow2(0.5)

Artur = Student(name="Artur", height=165)
print(Artur)
print(Artur.height)
print(Artur.name)
Artur.grow(2)
print(Artur.height)

#print(Serg.count_of_Student)
#print(Serg.count_of_Student)
