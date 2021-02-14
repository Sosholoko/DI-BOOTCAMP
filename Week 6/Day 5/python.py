# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict["class"]["student"]["marks"]["history"])

#Exercise 1


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict = {keys[i]: values[i] for i in range(len(keys))}

# print(dict)


# for key, value in zip(keys, values):
#     print(key, value)


#Exercise 2

# cost = 0
# age = int(input("What's your age when finished enter exit"))

# while age != 'exit':
#     if age < 3:
#         cost = 0
#         print("You go free")
#         age = int(input("What's your age when finished enter exit"))
#     elif age > 3 and age < 13:
#         cost = cost + 10
#         print("Your ticket price is 10$")
#         age = int(input("What's your age when finished enter exit"))
#     elif age > 12:
#         cost = cost + 15
#         print("Your ticket price is 15$")
#         age = int(input("What's your age when finished enter exit"))
#     else:
        
#         break

# print(cost)        



#Exercise 3

# brand = {
# "name": "Zara", 
# "creation_date": 1975,
# "creator_name": "Amancio Ortega Gaona", 
# "type_of_clothes": ["men", "women", "children", "home"], 
# "international_competitors": ["Gap", "H&M", "Benetton"], 
# "number_stores": 7000, 
# #"major_color": ("France": "blue", "Spain": "red", "US": "pink", "green")
# }

# brand["number_stores"] = 2

# print(brand["number_stores"])

# brand["Country creation"] = "Spain"
# print(brand)

# if "international_competitors" in brand:
#     brand["international_competitors"] = "Gap", "H&M", "Benetton", "Desigual"
# else:
#     print("okay")

# print(brand)

# del brand["creation_date"]

# print(brand)
# print(brand["international_competitors"][-1])

# print(len(brand))

# print(brand.keys())

# more_zara ={
#     "creation_date": 1975 
#     "number_stores": 10 000 
# }

# brand.update(more_zara)

# print(brand)


#Exercise 4

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

disney_users_1 = { i : range(0, len(users)) for i in users}

print(disney_users_1)

disney_users_2 = { i : users[i] for i in range(0, len(users) ) }

print(disney_users_2)