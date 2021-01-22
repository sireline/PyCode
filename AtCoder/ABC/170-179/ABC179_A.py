N = int(input())
X = []
Y = []
for i in range(N):
    x, y = [int(n) for n in input().split()]
    X.append(x)
    Y.append(y)
for i in range(N):
    ans = 1
    for j in range(N):
        if (X[i]>X[j] and Y[i]>Y[j]) or (X[i]<X[j] and Y[i]<Y[j]):
            print((X[i], Y[i]), (X[j], Y[j]))
            ans += 1
    print(ans)
