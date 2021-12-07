from __future__ import print_function


class Money:
    def __init__(self):
        self.__long = 1
        self.__byte = 1

    def set_nothing(self):
        pass

    def set_long(self, long):
        self.__long = long

    def set_byte(self, byte):
        self.__byte = byte

    def get_long(self):
        return self.__long

    def get_byte(self):
        return self.__byte

    def to_string(self):
        value = float(str(self.__long) + "." + str(self.__byte))
        return value

    def read(self):
        self.set_long(input("Введіть кількість гривень: "))
        self.set_byte(input("введіть кількість копійок: "))

    def __sub__(self, other):
        print(self.to_string() - other)

    def __mul__(self, other):
        print(self.to_string() * other)

    def compere(self, other):
        if self.to_string() > other:
            print("перше значення більше")
        elif self.to_string() < other:
            print("друге число більше")
        else:
            print("вони рівні")

    def increment(self):
        x = self.to_string()
        x += 1
        print(x)

    def decrement(self):
        x = self.to_string()
        x -= 1
        print(x)

    def __str__(self):
        pass
