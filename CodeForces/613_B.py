N = int(input())
for i in range(N):
    n = int(input())
    A = [1 for a in input().split() if int(a)<0]
    print('NO' if sum(A) else 'YES')
