#Daily challenge

import datetime


birth_year = int(input("What's your birth year ? /YYYY/\n"))
birth_month = int(input("What's your birth month ? /MM/\n"))
birth_day = int(input("What's your birth day ? /DD/\n"))

d = datetime.datetime.today().day
m = datetime.datetime.today().month
y = datetime.datetime.today().year

#birthday is equal to today year minus the user date

bd = y - birth_year

#if positive so minus one to the birth year

if birth_month - m > 0:
    bd = bd-1
candle = bd % 10
f = ("i" * candle)






print(      f"-{f}-")
print("   |:H:a:p:p:y:|")
print(" __|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")


