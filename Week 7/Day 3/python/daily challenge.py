#Daily Challenge



def div_by_zero(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print(0)

div_by_zero(5,0)