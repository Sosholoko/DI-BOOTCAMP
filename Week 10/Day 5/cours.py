# We will create a program that will ask the user for a word. It will check if the word is a valid English word, and then find all possible anagrams for that word.

# First Download this text file

#     In a new file called anagram_checker.py, create a class called AnagramChecker
#     The class should have the following methods:
#         __init__ - should load the word list file (text file) into a variable, so that it can be searched later on.
#         is_valid_word(word) – should check if the given word (‘word’) is a valid word.
#         get_anagrams(word) – should find all anagrams for the given word. (eg. if ‘word’ is ‘meat’,the function should return a list containing [‘mate’, ‘tame’, ‘team’].)
#         (Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain exactly the same letters (but not in the exact same order), and False if not.)
#         Note: None of the methods of this class should print anything to output.
#     Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.
#     It should do the following:
#         Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
#         If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then validated:
#             Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
#             Only alphabetic characters are allowed. No numbers or special characters.
#             Whitespace should be removed from the start and end of the user’s input.
#         Once your code has decided that the user’s input is validated, it should find out:
#             if the user’s word is a valid English word, and all possible anagram words for the user’s word.
#             The above steps should be done by an instance of the AnagramChecker class.
#             Display the information about the word to the user in a user-friendly, nicely-formatted message on the screen. Something like this: 


import json
import tkinter as tk
from tkinter.messagebox import *
from tkinter import *
from tkmacosx import Button as button
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


class AnagramChecker():
    def __init__(self):
        file = open("/Users/sashakharoubi/Desktop/BOOTCAMP/Week 10/Day 5/text.txt", "r")
        f = file.read()
        self.wordlist = f.lower().split('\n')
        file.close()

    def is_valid_word(self, user_word):
        if user_word in self.wordlist:
            ans = f"Yes the word {user_word} is in the list"
            blank.insert(0, ans)
        else:
            ans2 = f"No the word {user_word} not in the list"
            blank.insert(0, ans2)
        
        
    def get_anagrams(self, user_word):
        for word in self.wordlist:
            if set(user_word) == set(word):
                if len(user_word) == len(word):
                    answ = " " + word
                    blank2.insert(0, answ)



#na.is_valid_word("cat")
#ana.get_anagrams("meat")


root = tk.Tk()
ana = AnagramChecker()

def del_value(event): # note that you must include the event as an arg, even if you don't use it.
    entry.delete(0, "end")
    blank.delete(0, "end")
    return None

def checkdelete(word):
    ana.is_valid_word(word)
    clear_text()

def pushdelete(word):
    blank2.delete(0, "end")
    ana.get_anagrams(word)
    


def clear_text(self):
    blank.delete(0, "end")
    blank2.delete(0, "end")






HEIGHT = 800
WIDTH = 400


root.title("Anagram Checker")
root.minsize(400, 800)

canvas = tk.Canvas(root, height= HEIGHT, width = WIDTH, bd=0, highlightthickness = 0)
canvas.pack()

frame = tk.Frame(root, bg="#222f3e")
frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

lower_frame = tk.Frame(root, bg="#E9E9E9", bd=0, highlightthickness = 0, relief="sunken")
lower_frame.place(relx = 0.1, rely = 0.1, relwidth=0.8, relheight=0.8)


entry_txt = tk.Label(lower_frame, text="Welcome to ANAGRAM CHECKER", font=("Montserrat", 15), bg="#E9E9E9", fg="black")
entry_txt.pack(side = "top")

entry = tk.Entry(lower_frame, bg="#E9E9E9", fg='black', bd=0)
entry.insert(0, "Choose a word to check")
entry.bind("<Button-1>", del_value)
entry.pack(side = 'top')

blank = tk.Entry(lower_frame)

blank2 = tk.Entry(lower_frame)


blank.pack(expand = "yes")

blank2.pack(side = "top")

clear = button(lower_frame, text ="Clear", bg = "red", fg="white", command = clear_text)
clear.pack(expand = "yes")

confirm = button(lower_frame, text='Check Word', bg ='blue', fg="white", command = (lambda: checkdelete(entry.get())))
confirm.pack(expand = "yes")

confirm2 = button(lower_frame, text='Check Anagram', bg ='blue', fg="white", command = (lambda: pushdelete(entry.get())))
confirm2.pack(expand = "yes")







root.mainloop()