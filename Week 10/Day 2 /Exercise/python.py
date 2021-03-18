#Exercise 2

import random
import string
from googletrans import Translator

# numb = random.randint(1, 100)


# def num1():
#     return random.randrange(1, 100)



# while True:
#     r = num1()
#     if r == numb:
#         print("Success")
#         break
#     else:
#         print("still not")


#Exercise 3


# def get_random_string(length):

#     letters = string.ascii_lowercase
#     letters2 = string.ascii_uppercase
#     result_str = ''.join(random.choice(letters) + random.choice(letters2) for i in range(length))
#     print("Random string of length", length, "is:", result_str)

# get_random_string(5)


#Daily Challenge

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# english_words = []

# translator = Translator()

# translation = translator.translate(french_words[0], dest='en')

# for word in french_words:
#     translation = translator.translate(word, dest='en')
#     english_words.append(translation.text)

# print(english_words)