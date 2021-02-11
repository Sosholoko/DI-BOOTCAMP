# Daily Challenge

import random

word = input("Choose a word of 10 characters long\n") #make a break line
first_char = word[0]
last_char = word[-1]

if len(word) < 10:
        print("It must be 10 characters long")
elif len(word) > 10:
        print("String too long, must be 10 max")
else:
        print(first_char, last_char)

if len(word) < 10:
    print("It must be 10 characters long")
elif len(word) > 10:
    print("String too long, must be 10 max")
else:
    for i in range(0, len(word)):
        print(word[:i+1])

print(word.split(","))
#print(random.shuffle(word))
