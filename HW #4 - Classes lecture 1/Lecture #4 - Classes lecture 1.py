#1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed, mileage_info
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage =  mileage

    def increase_speed(self):
        print('increase_speed')
    def break_speed(self):
        print('break_speed')
    def mileage_info(self):
        print('mileage_info')


# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод seating_capacity

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
    def seating_capacity(self,  capacity):
        print(f"The seating capacity of the bus is {capacity}")


# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
print(issubclass(Bus, Vehicle))

#4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus

school_bus = Bus(60, 12345)

print(isinstance(school_bus, Vehicle))
print(isinstance(school_bus, Bus))
# 5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address, main_subject

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students
    def school_address(self, address):
        self.address = address
        print(f'School address is {self.address}')
    def main_subject(self, subject):
        self.subject = subject
        print(f'Main subject - {self.subject}')

school_29 = School(2345, 350)
school_29.school_address('Ukraine, Kyiv city')
school_29.main_subject('English')
# 6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний -    bus_school_color

class SchoolBus(School, Bus):
    def bus_school_color(self, color):
        print(f'Bus school color is {color}')
school_bus_111 = SchoolBus((123, 500),(120, 1000))
school_bus_111.bus_school_color('blue')


# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
# створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.
class Bear:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print('likes to eat fish')

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print('likes to eat meat')

gammy = Bear('Gammy', 'brown')
fang = Wolf('Fang', 'white')

for animal in (gammy, fang):
    animal.eat()

# Магічні методи:
# Додатково:
# 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу,
# лише коли population > 1500, # інакше повертається повідомлення: "Your city is too small".
# Підказка: використовуєте для цього завдання магічні методи
class City:
    def __new__(cls, name, population):
        if population > 1500:
            return object.__new__(cls)
        else:
            print (f"{name} - your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population
        print (f'{self.name} - good city')

city1 = City('Kharkiv', 2000)
city2 = City('Poltava', 1000)
