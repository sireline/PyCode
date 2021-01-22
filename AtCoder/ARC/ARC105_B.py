from math import gcd

N = int(input())
A = set([int(n) for n in input().split()])

def r(i):
    if i == len(A)-1:
        return gcd(A[i], A[i+1])
    return gcd(r(i) , r(i+1))

    for i in range(len(A)):
    print(gcd(A))