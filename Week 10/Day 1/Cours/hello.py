def add(a, b):
    result = a + b
    if result < 0:
        return 0
    else:
        return result

def sub(a, b):
    result = a - b
    if result < 0:
        return 0
    else:
        return result


def div(a, b):
    result = a / b
    if result < 0:
        return 0
    else:
        return result

def mult(a, b):
    result = a * b
    if result < 0:
        return 0
    else:
        return result

print(mult(20, 87))
