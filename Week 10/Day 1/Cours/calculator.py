import hello

print("Welcome to our special calculator where no result is under 0")
print("Choose an operation:")
print("a) Add")
print("b) Substract")
print("c) Multiply")
print("d) Divide")

user_choice = input("> ") # a, b, c, or d

number1 = int(input("Please give me a number: "))
number2 = int(input("Please give me another number: "))

if user_choice == "a":
    print("You selected the Addition")
    print(hello.add(number1, number2))
elif user_choice == "b":
    print("You selected the Substraction")
    print(hello.sub(number1, number2))
elif user_choice == "c":
    print("You selected the Multiplication")
    print(hello.mult(number1, number2))
elif user_choice == "d":
    print("You selected the Division")
    print(hello.div(number1, number2))
else:
    print("Incorrect input")