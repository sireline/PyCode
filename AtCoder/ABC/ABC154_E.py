N = int(input())
K = int(input())
c = 0
for i in range(1, N+1):
    if len(str(i).replace('0', '')) == K:
        c += 1
print(c)
