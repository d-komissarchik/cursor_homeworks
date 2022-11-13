# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
# Example:
#
# for i in FibonacciNumbers(10):
#     print(i)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

class FibonacciNumbers:
    num1, num2 = 0, 1
    def __init__(self, max_count):
        self.max_count = max_count

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_count > 0:
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.max_count -= 1
            return self.num1
        else:
            raise StopIteration
for i in FibonacciNumbers(10):
    print(i)

# 2.* Implement generator for Fibonacci numbers
def generator(n):
    num1, num2 = 0, 1

    for i in range(n):
        num1, num2 = num2, num1 + num2
        yield num1

fib_gen = generator(10)
for i in fib_gen:
    print(i)

# 3. Write generator expression that returns square numbers of integers from 0 to 10
def generator(range):
    number, squared = 0, 0
    while range > 0:
        squared = number * number
        number += 1
        range -= 1
        yield squared


my_squared_list = generator(11)
for i in my_squared_list:
    print(i, end=' ')
print('\n')
# or
print(*[i * i for i in range(11)])
# or
square_num = (num ** 2 for num in range(11))
for j in square_num:
    print(j, end=' ')

# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def Screen(self):
        raise NotImplementedError

    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def WebCam(self):
        raise NotImplementedError

    @abstractmethod
    def Ports(self):
        raise NotImplementedError

    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def Screen(self):
        print("Screen")

    def Keyboard(self):
        print("Keyboard")

    def Touchpad(self):
        print("Touchpad")

    def WebCam(self):
        print("WebCam")

    def Ports(self):
        print("Ports")

    def Dynamics(self):
        print("Dynamics")


# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.

class Car(ABC):
    def drive(self):
        print("Driving a car")

    def stop(self):
        print("Stopping a car")

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError

