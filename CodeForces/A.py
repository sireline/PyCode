t = int(input())
for i in range(t):
    n = 0
    ans = 0
    k = int(input())
    s = list(input())[::-1]
    for c in s:
        if c=='P':
            n += 1
        else:
            if ans < n:
                ans = n
            n = 0
    print(ans)
