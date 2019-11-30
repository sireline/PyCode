N, r = [int(n) for n in input().split()]
for i in range(N):
    m = min([int(n) for n in input().split()])
    if m >= r*2:
        print(i+1)
