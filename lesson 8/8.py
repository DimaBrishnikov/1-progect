class MyException(Exception):
    def __init__(self, mydate):
        self.date = mydate
    def __str__(self):
        return f"{self.date}Це мій класс винятку"


a = int(input())
b = int(input())
try:
    try:
        if b ==0:
            raise MyException("15.02.2023")
            #raise ZeroDivisionError(f"Спроба дылення на{b}")
        print(a/b)
        #print(name)

    except (ZeroDivisionError) as error:
        print(error)
    else:
        print("Проблем не виявлено")
    finally:
        print("Все одно щось виконаю")
except MyException as error:
    print(error)

except:
    print("Невідома помилка")

print('Кінець програми')



'''except NameError:
    print("Помилка не відоме ім'я!!!")'''