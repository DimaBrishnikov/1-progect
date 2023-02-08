class Human:
    height = 170
    __age = 30
    gladness = 50


class Student(Human):
    pass


class Aspirant(Student):
    height = 180
    def __init__(self):
        print(self.height)
        #print(self.age)
        print(self.gladness)

    def _hello(self):
        print("hello")


    def _hello(self):
        print("hello")


class Worker(Human):
    age = 35


class Hello:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"



    def __init__(self):
        self.kitty = "__kitty"
        self._kitty = "__kitty"
        self.__kitty = "__kitty"


class Hello_kity:
    pass


    def __method(self):
        print("Method")
'''class Hi(Hello_kity):
    def hi_print(self):
        super().__method()
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.kitty)
        print(self._kitty)
        print(self.__kitty)'''


        
class Computer:

    def __init__(self):
        self.RAM = "16 GB"
        super().__init__()
        self.model = None


     def calc(self):
         print("Calculate....")



 class Monitor:
     def __init__(self, *):
         super().__init__()
         self.resolution = "8K"
     def display(self):
         print("Print result")

 class  SmartPhone(Monitor, Computer):
     def info(self):
         print(self.resolution)
         print(self.RAM)



phone = SmartPhone()
phone.info()




'''hello = Hello_kity()
hello.print()'''

"""hi = Hi()
hi.hi_print()""""""




"'''asp = Aspirant()
asp.__age = 10000''''''




'''st = Student()
wr = Worker()
print(st.age)
print(wr.age)'''''''''