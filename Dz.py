class Animal:

    def __init__(self, name=None, weight=None, satisfying=100):
        self.name = name
        self.weight = weight
        self.satisfying = satisfying

    def __str__(self):
        return f"Я {self.name}, мій в вага {self.weight} см я ситий на  {self.satisfying}"




Barsick = Animal(name="Barsick", weight=5.6, satisfying=100)
print(Barsick)

Zefir = Animal(name="Zefir", weight=10.5, satisfying=100)
print(Zefir)
