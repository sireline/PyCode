X = int(input())

def is_prim(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return n != 1

for i in range(X, 10**9+1):
    if is_prim(i):
        print(i)
        break


