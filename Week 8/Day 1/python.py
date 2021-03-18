# class Human():
#     def sleep(self):
#         print("Zzzzzzzz....")
#         print(self)


# bob = Human()
# bill = Human()

# bill.sleep()
# bob.sleep()

class Animal():
    def __init__(self, name, eye_color, age, speed):
        self.eye_color = eye_color
        self.age = age
        self.name = name
        self.speed = speed
        #print(f"{name} is {age} years old and has {eye_color} eyes")

    def introduce(self):
        print(f"{self.name} is {self.age} years old and has {self.eye_color} eyes")

    def birthday(self):
        print(f"Happy Birthday {self.name} you're now {self.age + 1} years old")
        self.age += 1

    def run(self, distance):
        #print(f"{self.name} will take {distance/self.speed} minutes to travel")
        return distance/self.speed

    def say_hello(self, other):
        """
        Say hello to an other human
        """
        print(f"{self.name} says hello to {other.name}")

    def race(self, other, distance):
        
        self.time = self.run()
        other.time = other.run()

        if self.time < other.time:
            print(f"{self.name} arrived first {self.speed} seconds and {other.name} arrived after {other.speed} seconds")
        elif other.time > self.time:
            print(f"{other.name} arrived first {other.speed} seconds and {self.name} arrived after {self.speed} seconds")
        else:
            print(f"{self.name} and {other.name} arrived at the same time")

simba = Animal("Simba","blue", 11, 9)
pumba = Animal("Pumba","green", 15, 4)
marty = Animal("Marty","gray", 18, 7)

simba.race(pumba, 35)


