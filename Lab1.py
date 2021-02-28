import math


def Complement(n):
    bits = int(math.floor(math.log(n) / math.log(2))) + 1
    return ((1 << bits) - 1) ^ n


def execute():
    n = int(input("Enter a number: "))
    print("Inverted number: ")
    print(Complement(n))


execute()
