def M91(n):
    if n > 100:
        return n-10
    else:
        return M91(M91(n+11))
def main():
    n = eval(input("Enter the value of n"))
    print(M91(n))

main()
#Values tested were 50 and 150
#For 50, 91 was returned as expected
#For 150, 140 was resturned as expected
#The function returns 91 for any n <=101
#Otherwise, it returns the value n - 10
