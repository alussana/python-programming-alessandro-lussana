import math

def second_degree(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        return([x1, x2])
    else:
        print("Sorry bruh, delta is negative")

print(second_degree(2,4,2))
