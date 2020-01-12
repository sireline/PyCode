t = int(input())
for i in range(t):
    n = int(input())
    a = [int(n) for n in input().split()]
    ans = max(a) - min(a)
    if  ans >= n:
        print('YES')
        print(1, n)
    else:
        print('NO')
