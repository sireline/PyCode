N = int(input())
A = [int(n) for n in input().split()]
AS = sorted(set(A))
ans = 0
if len(AS) == 1:
    print(ans)
    exit()
ans += 1
for i in range(1, len(AS)):
    c = 0
    for j in range(i):
        if AS[i] % AS[j]==0:
            break
        else:
            c += 1
            if c == i:
                ans += 1
print(ans)
