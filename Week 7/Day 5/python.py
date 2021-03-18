import random

random_list = ["python", "javascript", "program", "bootcamp", "share"]
word = random.choice(random_list)

active = True
counter = 5
wrong =0
loop = 0
letter_list = list(word)
print(letter_list)
star_list =[]
used = []

for i in range(len(letter_list)):
    star_list.append("*")
print(star_list)
while active:
    if word == ''.join(star_list):
        active = False
        print("Winner!!")
    elif word != ''.join(star_list) and counter > 0:
        letter = input(f"Please input a letter, you have {counter} lives left")
        used.append(letter)
        for let in letter_list:
            if let == letter:
                star_list[loop] = let
            else:
                wrong += 1
            loop += 1
        if wrong == len(letter_list):
            counter = counter - 1
        else:
            print("".join(star_list))
            print(f"{counter} lifes left")
        wrong = 0
        loop = 0
        print(used)
    elif counter == 0:
        active = False
        print("You lost")
print("finished")





