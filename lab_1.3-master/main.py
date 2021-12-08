from __future__ import print_function
from overload import Overloads


class Money:
    def __init__(self):
        self.byte = None
        self.long = None

    def set_nothing(self):
        pass

    def set_long(self, long):
        self.long = long

    def set_byte(self, byte):
        self.byte = byte

    def get_long(self):
        return self.long

    def get_byte(self):
        return self.byte

    def read(self):
        self.set_long(input("Введіть кількість гривень: "))
        self.set_byte(input("введіть кількість копійок: "))

    def to_string(self):
        value = float(str(self.long) + "." + str(self.byte))
        return value


class Methods(Money):
    def sub(self, first, second):
        self.long = first
        self.byte = second
        return Overloads(self.long) - Overloads(self.byte)

    def mul(self, first):
        self.long = first
        return Overloads(self.long) * Overloads(float(input("Введіть дробове число: ")))

    def compere(self, first, second):
        self.long = first
        self.byte = second
        if self.long > self.byte:
            return "перше значення більше"
        elif self.long < self.byte:
            return "друге число більше"
        else:
            return "вони рівні"

    def increment(self, first):
        self.long = first
        x = self.long
        x += 1
        return x

    def decrement(self, first):
        self.long = first
        x = self.long
        x -= 1
        return x

