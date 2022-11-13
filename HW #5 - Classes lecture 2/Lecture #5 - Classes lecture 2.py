# 1. Make the class with composition

class Laptop:
    def __init__(self):
        slot_1 = Battery('First battery 4500mAh')
        slot_2 = Battery('Second battery 6000mAh')
        self.batteries = [slot_1.capacity, slot_2.capacity]


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


laptop = Laptop()
print(laptop.batteries)


# 2. Make the class with aggregation
class Guitar:
    def __init__(self, string):
        self.string = string


class GuitarString:
    def __init__(self, material):
        self.material = material


guitar_string = GuitarString('metal')
electro_guitar = Guitar(guitar_string.material)
print(electro_guitar.string)

# 3 Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
class Calc:
    def __init__(self):
        pass

    @classmethod
    def add_nums(cls, a, b, c):
        return a + b + c


result = Calc()
print(result.add_nums(2, 2, 1))
print(Calc.add_nums(3, 3, 4))



#4*.
""" Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
    Він повинен мати 2 методи:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']"""

class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])

pasta_1 = Pasta(["tomato", "cucumber"])
print(f'{pasta_1.__class__.__name__} ingredients will equal to', pasta_1.ingredients)
pasta_2 = Pasta.bolognaise()
print(f'{pasta_2.__class__.__name__} ingredients will equal to', pasta_2.ingredients)

#5*
"""Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50"""

class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value > Concert.max_visitors_num:
            self._visitors_count = Concert.max_visitors_num
        else:
            self._visitors_count = value


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

#6."""Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str),
# email (str), birthday (str), age (int)"""
    
import  dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: str

#7. Create the same class (6) but using NamedTuple
import collections

AddressBookClass = collections.namedtuple('AddressBookClass', ['key', 'name', 'phone_number', 'address', 'email',
                                                               'birthday', 'age'])

adressbook = AddressBookClass(111, 'Dima', '0631234567', 'Kyiv', 'email@kyiv.com', '23.2.2000', '22')
print(adressbook.key)
print(adressbook[2])



#8.
"""Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', 
    address='', email='', birthday= '', age='')"""
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key= {self.key}, name= {self.name}, phone_number= {self.phone_number}, ' \
               f'address= {self.address}, email= {self.email}, birthday= {self.birthday}, age= {self.age})'

myadressbook = AddressBook(111, 'Dima', '0631234567', 'Kyiv', 'email@kyiv.com', '23.2.2000', '22')
print(myadressbook)

#9 Change the value of the age property of the person object

class Person:
    def __init__(self):
        name = "John"
        age = 36
        country = "USA"


setattr(Person, 'age', 55)
print(getattr(Person, 'age'))
#or Person.age = 55
#   print(Person.age)


#10
"""Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr"""

class Student:
    id = 0
    name = ""

mystudent = Student()
setattr(mystudent, 'email', 'mystudent@email.com')
student_email = getattr(mystudent, 'email')
print(student_email)

