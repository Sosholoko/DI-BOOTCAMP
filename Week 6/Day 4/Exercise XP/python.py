#Exercise 1

# fav_numbers = [3, 8, 16, 26]
# friend_num = [1, 7, 4]
# our_num = []

# fav_numbers.append(2)
# fav_numbers.append(9)

# del fav_numbers[-1]

# our_num.append(fav_numbers + friend_num)

# print(our_num)


#Exercise 3

# numbers = range(1, 21)

# for i in numbers:
#     print(i)

#Exercise 5

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# del basket[0]
# del basket[-1]
# basket.append("Kiwi")
# basket.insert(0,"Apples")
# bb = basket.count("Apples")
# empty = basket
# del empty[:]
# basket = empty


# print(bb)

# print(basket)


#Exercise 6


# value = ""

# while value != "Sasha":
#     value = input("What's my name ?\n")
#     if value != "Sasha":
#         print("No what's my name ? \n")
#     else:
#         print("yeah you got it")

#Exercise 7



#Exercise 8

# mult = range(3, 31)
# number_user = 3

# for i in mult:
#      print(i * number_user)


#Exercise 10

# fruits_users = input("Enter fruits separated by a ',' ")
# split_fruit = fruits_users.split(', ')

# choice_fruit = input("Which fruit do you want ?\n")
# if choice_fruit in split_fruit:
#     print("Okay you chose from your own fruits")
# else:
#     print("Alright hope you'll enjoy !")

#Exercise 11


# active = True
# topping = input("Which toppings you want to add ? When finished enter done\n") 
# tab = []

# while active == True:
#     if topping == "done":
#         active == False
#         print("Alright, here's your resume")
#         break
#     else:
#         active == True
#         topping = input("Topping Added, What else\n")


#Exercise 13

# users_list = ["Jason", "Mark", "John", "Daisy"]
# accepted_user = []


# for user in users_list:
#     print("Let's check everybody's age")
#     age = int(input(f"{user} how old are you ?"))
#     if age >= 16:
#         accepted_user.append(user)
# print(f"Heres are the accepteds users, {accepted_user})


#Exercise 14

user = []
active = True


while active:
    print("Confirm with yes or Deny with no")
    answer = input("Do you want to add a name ? yes or no\n")
    if answer == "yes":
        name = input("What's your name ?")
        user.append(name)
    elif answer =="no":
        remove = input("Do you want to remove a name ?\n")
        if remove == "yes":
            remove_name = input("Which name to remove ?\n")
            user.remove(remove_name)
        elif remove == "no":
            print(user)
            active == False









