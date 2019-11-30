import math

N = int(input())
X = []
Y = []
for i in range(N):
    x, y = [int(n) for n in input().split()]
    X.append(x)
    Y.append(y)
L = []
for i in range(N-1):
    for j in range(i+1, N):
        L.append(math.sqrt((X[i]-X[j])**2 + (Y[i]-Y[j])**2))
        print(L)
ans = []
for i in range(len(L)-1):
    for j in range(i+1, len(L)):
        ans.append(L[i]+L[j])
        print(ans)
print(sum(ans)/len(ans))