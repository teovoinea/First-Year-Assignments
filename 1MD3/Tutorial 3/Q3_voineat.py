def factorial(x):
    if (x == 1):
        return 1;
    else:
        return x * factorial(x-1);
def Cfac(n, k):
    return (factorial(n))/(factorial(k)*factorial(n-k));
def Crec(n, k):
    if (1 <= k and k < n):
        return (Crec(n-1, k-1) + Crec(n-1, k));
    else:
        return 1;
def main():
    n, k = eval(input("Enter n, k separated by commas"));
    print("Cfac: " + str(Cfac(n, k)) + " Crec: " + str(Crec(n, k)));

main()
#Functions were tested with the values 9, 3 which returned 84 for both functions
#Results were compared to the results from http://www.ohrt.com/odds/binomial.php
#Confirmed 84
#I think Cfac will return the value faster than Crec because there is only
#one instruction in the entire function which is recursive
#Also, Crec will require more recursive calls
