#Exercise 1

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def Oldest(*args):
#         return max(args)


# mickey = Cat("Mickey", 11)
# mini = Cat("Mini", 8)
# coop = Cat("Coop", 86)


# print(f"The oldest cat is {Oldest(mickey.age,mini.age,coop.age)} years old")


#Exercise 2

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#     def Bark():
#         print("goes woof")
#     def Jump(x):
#         print(f"jump {x*2} cm high")
    

# davids_dog = Dog("Rex", 50)
# sarahs_dog = Dog("TeaCup", 20)

# print(davids_dog.name, davids_dog.height)
# print(sarahs_dog.name, sarahs_dog.height)

# if davids_dog.height < sarahs_dog.height:
#     print(f"{davids_dog.name} is not bigger than {sarahs_dog.name}")
# elif davids_dog.height > sarahs_dog.height:
#     print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")


#Exercise 3

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def sing(self):
#         print(self.lyrics)

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing()


#Exercise 4

# class Zoo:
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#     def add_animal(new_animal):
#         if new_animal not in animals:
#             animals.append(new_animal)
#         else:
#             pass
#     def get_animal(zoo_name):
#         print(zoo_name +animals)
#     def sell_animal(animal_sold):
#         if animal_sold in animals:
#             animals.remove(animal_sold)
#         else:
#             pass
    

# toury = Zoo("Toury")

# toury.get_animal(x)


# Daily Challenge

class Farm:
    
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def get_info(self):
        
        msg = ""
        msg += f"{self.name}'s Farm" + "\n"
        msg += "\n"

        for animal, count in self.animals.items():
            msg += f"{animal}: {count}" + "\n"
        
        return msg

        
        # print(f"{macdonald.name}'s Farm\n {self.animals}")
        #return self.animals

    def add_animal(self, animal, *count):
        if animal in self.animals.keys():
            self.animals[animal]+= count
        else:
            self.animals[animal] = count

        # self.animals.append(animal)
        # return self.animals


macdonald = Farm("Macdonald")
macdonald.add_animal("jaja")
macdonald.add_animal("jaja")
macdonald.add_animal("tiger", 3)
#print(macdonald.animals)
print(macdonald.get_info())