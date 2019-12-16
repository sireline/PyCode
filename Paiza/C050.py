S, a, b = [int(n) for n in input().split()]
P = [('A', 10, a), ('B', 1000, b)]
i = 0
while True:
    S += P[i%2][1]
    if P[i%2][2] < S:
        print(P[(i-1)%2][0], S-P[i%2][1])
        break
    i += 1
