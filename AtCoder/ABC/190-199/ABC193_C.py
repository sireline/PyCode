import math

N = int(input())
X = []
ans = 0
for a in range(2, int(N**0.5)+1):
    for b in range(2, int(math.log(N, a))+1):
        x = a**b
        y = b**a
        if x <= N:
            if x not in X:
                X.append(x)
                ans += 1
        elif y <= N:
            if y not in X:
                X.append(x)
                ans += 1
        else:
            break
print(N-ans)
