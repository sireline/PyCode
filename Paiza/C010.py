a, b, R = [int(n) for n in input().split()]
N = int(input())
for i in range(N):
    x, y = [int(n) for n in input().split()]
    ans = (x-a)**2+(y-b)**2
    print('silent' if ans >= R**2 else 'noisy')
