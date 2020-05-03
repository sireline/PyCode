from itertools import permutations

N = int(input())
X = []
Y = []
for i in range(N):
    x, y = [int(n) for n in input().split()]
    X.append(x)
    Y.append(y)

def dist(i, j):
    dx = X[i] - X[j]
    dy = Y[i] - Y[j]

    return math.sqrt(dx*dx + dy*dy)

P = [i for i in range(N)]
len = 0
cnt = 0

while True:
    for i in range(N-1):
        len += dist(P[i], P[i+1])
    cnt += 1
    if :
        break
