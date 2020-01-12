t = int(input())
for i in range(t):
    n, k1, k2 = [int(n) for n in input().split()]
    a = [int(n) for n in input().split()]
    b = [int(n) for n in input().split()]
    print('YES' if max(a) > max(b) else 'NO')
