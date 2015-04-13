from math import *
def main():
    value = eval(input("Please enter a number"))
    print(oneThird(value))
def oneThird(rep):
    value = 0
    for i in range(1, rep + 1):
        value += pow(i, 2)
    value = value / pow(rep, 3)
    return value
main()
