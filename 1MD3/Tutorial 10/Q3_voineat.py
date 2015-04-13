def magicsquare(n):
    J = [range(1, n+1)] * n
    I = [list(a) for a in zip(*J)]
    A = [[(I[i][j] + J[i][j] + (n-3)/2) % n for i in range(n)] for j in range(n)]
    B = [[(I[i][j] + 2*J[i][j] - 2) % n for j in range(n)] for i in range(n)]
    return [[n*A[i][j] + B[i][j] + 1 for j in range(n)] for i in range(n)]
def printsquare(l):
    for i in l:
        for j in i:
            print(int(j), "  ", end = "")
        print("")

    
