A, B, K = [int(n) for n in input().split()]
x = []
for i in range(1, min(A, B)+1):
    if A%i == 0 and B%i ==0:
        x.insert(0, i)
print(x[K-1])
