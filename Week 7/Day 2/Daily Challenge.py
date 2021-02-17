# import math
# import os
# import random
# import re
# import sys

# first_multiple_input = int(input().rstrip().split())

# n = int(first_multiple_input[0])
# m = int(first_multiple_input[1])

# matrix = []

# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)

# # start   
# matrix = list(zip(*matrix))

# sample = str()

# for words in matrix:
#     for char in words:
#         sample += char

# print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample)) 


matrix = [
    ['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!'],
]


string_print = ''
for i in range(len(matrix[0])):
    for n in range(len(matrix)):
        letter = matrix[n][i]
        if letter.isalpha():
            string_print += letter
        else:
            if string_print:
                if string_print[-1] != ' ':
                    string_print += ' '



print(string_print)