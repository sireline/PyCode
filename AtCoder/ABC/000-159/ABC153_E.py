H, N = [int(n) for n in input().split()]
AB = []
for i in range(N):
    a, b = [int(n) for n in input().split()]
    AB.append((a, b, a/b))
ABP = sorted(AB, key=lambda x: (-x[2], x[1]))
j = 0
c = 0
while H > 0:
    if H >= ABP[j][0]:
        H -= ABP[j][0]
        c += ABP[j][1]
    elif H < min([n[0] for n in ABP]):
        H = 0
        c += min([n[1] for n in ABP])
    else:
        j += 1
print(c)
