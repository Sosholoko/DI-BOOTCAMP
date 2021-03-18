#Exercise 1


# class Pets():
    
#     def __init__(self, animals):
#         self.animals = animals
#         self.my_cats = []

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Baddies(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# mouse = Cat("Mouse", 7)
# tick = Cat("Tick", 9)
# pock = Cat("Pock", 12)


# my_cats = [Bengal("Mouse", 7), Chartreux("Tick", 9), Baddies("Pock", 12)]

# cats = Pets(my_cats)

# cats.walk()




#Exercise 2
import random

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def Bark(self):
        return f"WOOF, {self.name} is barking"
    
    def run_speed(self):
        return self.weight/(self.age*10)
        

    def Fight(self, other_dog):
        # self.power = self.run_speed + self.weight
        # other_dog.power = other_dog.run_speed + other_dog.weight

        # if self.run_speed > other_dog.run_speed:
        #     print(f"The fight was won by {self.name}, {self.other_dog} lost the fight")
        # else:
        #     print(f"The fight was won by {self.other_dog}, {self.name} lost the fight")

        if (self.weight*self.run_speed()) > (other_dog.weight*other_dog.run_speed()):
            return f"{self.name} won the fight"
        else:
            return f"{other.dog} won the fight"

caramel = Dog("Caramel", 11, 35)
fogi = Dog("Fogi", 8, 36)
denver = Dog("Denver", 14, 21)

print(caramel.Fight(fogi))




# #Exercise 3


class PetDog(Dog):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.trained = False
        

    def train(self):
        print(self.Bark())
        self.trained = True

    def Play(self, other_dog):

        dogs_names = ""
        

        for dog in other_dog:
            dogs_names += dog.name + ", "
            self.trained = False
            
        print(f"{dogs.name} play together")
    
    def do_a_trick(self):
        f"{self.name} do a barrel roll"
        f"{self.name} stands on their back legs"
        f"{self.name} shakes your hand"
        f"{self.name} plays dead"
        trick = random.randrange(0, 4)
                
        if self.trained == True:
            print(trick)
        else:
            print(f"{self.name} is not trained yet")

caramel.Play()




