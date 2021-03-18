class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __add__(self, other):
        print(self.age + other.age)

    def __repr__(self):
        return self.name


p1 = Person('sasha', 21)
p2 = Person("bob", 54)

p1.__add__(p2)