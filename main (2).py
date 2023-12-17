sol = []
def bkt (n):
    if n == 0:
        print (sol)
    else:
        for i in range (1,n+1):
            sol.append(i)
            bkt(n-i)
            sol.pop()
n = int(input())
bkt(n)