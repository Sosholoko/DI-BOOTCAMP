# def calculation (a,b):
#     return a+b, a-b

# calc = (calculation(2,4))

# print(calc)


# def display_message():
#     print("I'm currently learning about Python")

# display_message()

# def favorite_book(title):
#     print("One of my favorite books is" + title)

# favorite_book("Alice")


# def favorite_city(city, country="England"):
#     print (city +" "+ "is in" +" "+ country)

# favorite_city("Liverpool")
# favorite_city("London")
# favorite_city("New York", "United States")


# import random


# user_num = int(input("Choose a number\n"))

# def random_number(user_num):
#     random_number = random.randint(1, 100)


# while user_num != random_number:
#     print("Try Again")
#     user_num = int(input("Choose a number\n"))
#     random_number(user_num)
#     if user_num == random_number:
#         print("Success")
#         break


# random_number(user_num)


# def make_shirt(size, text):
#     print("You chose a T-Shirt at the size of" +" "+ size +" and a text that says" +" " + text)

# make_shirt("M", "Hello_World")
# make_shirt(text = "Hello_world", size="M")

magicians = ["Bozo", "Mador", "Mag"]
mag2 = ["Harry", "Ron", "Hermione"]

def show_magician(list_name):
    for name in list_name:
        print(name)

show_magician(mag2)

def make_great():
    great = ["The Great " + magician for magician in magicians]
    great = magicians
    print(magicians)
        
make_great()
