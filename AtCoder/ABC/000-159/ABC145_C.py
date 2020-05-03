N = int(input())
X = []
Y = []
for i in range(N):
    x, y = [int(n) for n in input().split()]
    X.append(x)
    Y.append(y)
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans += ((X[j]-X[i])**2 + (Y[j]-Y[i])**2)**0.5
print(ans*2/N)
