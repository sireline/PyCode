from itertools import product

N = int(input())
C = product(range(1,N+1), repeat=2)
print([c for c in C if str(c[0])[0] == str(c[1])[-1] and str(c[1])[0] == str(c[0])[-1]])
print(len([c for c in C if str(c[0])[0] == str(c[1])[-1] and str(c[1])[0] == str(c[0])[-1]]))
