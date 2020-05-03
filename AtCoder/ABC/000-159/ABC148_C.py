A, B = [int(n) for n in input().split()]
x = max(A, B)
y = min(A, B)
N = 10**5+1
for i in range(1, N):
    if (x*i)%y == 0:
        print(x*i)
        break

