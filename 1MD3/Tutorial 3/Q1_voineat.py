from math import *
def growth(a, p, n):
    x = a * pow((1 + (p/100)),n)
    return float(x)
def main():
    a, p, n = eval(input("Please enter a, p, n as comma separated numbers"))
    print(growth(float(a),float(p), float(n)))
main()
#The code was tested with the values
#10, 50, 3 which returned the expected result
#-10, 50, -3 which returned the expected result
