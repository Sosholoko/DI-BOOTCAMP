#Exercise 1

# class Program:
#     def __init__(self):
#         print("This function's purpose is to documentate about built-in function in Python")

#     @classmethod
#     def absolute(cls):
#         print("The abs() method returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.")

#     @classmethod
#     def integer(cls):
#         print("The int() method returns an integer object from any number or string.")
    
#     @classmethod
#     def inputraw(cls):
#         print("The raw_input() method reads a line from input, converts into a string and returns it.")
    

# python = Program()
# python.absolute()



#Exercise 2


# class Currency:
#     def __init__(self, name, summ):
#         self.name = name
#         self.summ = summ

#     def __str__(self): 
#         return f"{self.summ} {self.name}"
    
#     def __repr__(self):
#         return f"{self.summ} {self.name}"
    
#     def int(self):
#         return f"{self.summ}"

#     def add(self, num):
        


# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c4 = Currency('shekel', 1)
# c3 = Currency('shekel', 10)

# print(str(c1))
# print(repr(c1))
# print(c1 + 5)



#Daily Challenge

# list_name = []
# list_age = []
# list_score = []
# final = []

# def name():
    
    
#     n1 = input("What's your names")
#     list_name.append(n1)
#     n2 = input("What's your names")
#     list_name.append(n2)
#     n3 = input("What's your names")
#     list_name.append(n3)
#     n4 = input("What's your names")
#     list_name.append(n4)
#     n5 = input("What's your names")
#     list_name.append(n5)

# def age():

#     a1 = int(input("What's your age ? "))
#     list_age.append(a1)
#     a2 = int(input("What's your age ? "))
#     list_age.append(a2)
#     a3 = int(input("What's your age ? "))
#     list_age.append(a3)
#     a4 = int(input("What's your age ? "))
#     list_age.append(a4)
#     a5 = int(input("What's your age ? "))
#     list_age.append(a5)

# def score():

#     s1 = int(input("What's your score ? "))
#     list_score.append(s1)
#     s2 = int(input("What's your score ? "))
#     list_score.append(s2)
#     s3 = int(input("What's your score ? "))
#     list_score.append(s3)
#     s4 = int(input("What's your score ? "))
#     list_score.append(s4)
#     s5 = int(input("What's your score ? "))
#     list_score.append(s5)



# name()
# age()
# score()

# t1 = ((list_name[0]), (list_age[0]), (list_score[0]))
# final.append(t1)
# t2 = (list_name[1], list_age[1], list_score[1])
# final.append(t2)
# t3 = ((list_name[2], list_age[2], list_score[2]))
# final.append(t3)
# t4 = ((list_name[3], list_age[3], list_score[3]))
# final.append(t4)
# t5 = ((list_name[4], list_age[4], list_score[4]))
# final.append(t5)


# print(final)



# name()
# print(list_name)
# print((list_name[0]))

# age()
# print(list_age)

