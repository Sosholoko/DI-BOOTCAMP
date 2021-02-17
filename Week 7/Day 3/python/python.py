#my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]



# def sum_num(numbers):
#     summ = ''
#     for num in numbers:
#         if num.isdigit():
#             print(sum(num))
#         else:
#             print(num)


# sum_num(my_list)



# def sum_num(list_of_num):
#     total = 0
#     for num in list_of_num:
#         try:
#             total += num
#         except:
#             continue
#     return total

# print(sum_num(my_list))


# y = 2021
# m = 2
# gender = input("Are you male or female ?\n")

# def get_year():
#     user_year = int(input("What's your birth year ?\n"))
#     user_month = int(input("What's your birth month ?\n"))
#     current_y = y - user_year
#     current_m = m - user_month
#     if current_m < 0:
#         current_y = current_y - 1
#     return current_y





# def can_retire():
#     current_y = get_year()
#     if gender == "male":
#         if current_y > 67:
#             print("Yes you can retire Sir")
#         else:
#             print("You can't retire for now")
#     elif gender == "female":
#         if current_y > 62:
#             print("Yes you can retire Maam")
#         else:
#             print("No Maam, you cannot retire for now")

# can_retire()



# def digit_sum(x):
#     lst = [str(x)*i for i in range(1,x+1)]
#     print('+'.join(lst))
#     return sum(map(int, lst))

# digit_sum(3)

#from random import randrange




# def roll_dice():
#     count = 0
#     dice = randrange(1, 7)
#     dice2 = randrange(1, 7)
#     return dice, dice2


# def throw_until_double():
#     count = 0
#     dice, dice2 = roll_dice()
#     if dice == dice2:
#         print("Success")
#         return True
#     else:
#         print("No")
#         count = count + 1
#         throw_until_double()
#         return False


# throw_until_double()



# def get_full_name(fname, lname, *mname ):
#     name = (fname,lname) + mname
#     print(name)


# get_full_name("Sasha", "Kharoubi")


morse_code = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

code_reverse = {value:key for key,value in morse_code.items()}

def to_morse(word):
    print(' '.join(morse_code.get(i.upper()) for i in word))

def from_morse(word):
    print(''.join(code_reverse.get(i) for i in word.split()))


to_morse("189")
#from_morse(".... . .-.. .-.. ---")