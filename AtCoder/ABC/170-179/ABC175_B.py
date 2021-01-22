N = int(input())
L = [int(n) for n in input().split()]
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        if L[i]==L[j]:
            continue
        for k in range(j+1, N):
            if L[i]==L[k] or L[j]==L[k]:
                continue
            else:
                ls = sorted([L[i], L[j], L[k]])
                if ls[0]+ls[1] > ls[2]:
                    ans += 1
print(ans)
