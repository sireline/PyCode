N = int(input())
a = sorted([int(input()) for _ in range(N)], reverse=True)
f = 0
for i in range(N-3):
    if a[i] < a[i+1]+a[i+2]:
        f = sum([a[i], a[i+1], a[i+2]])
print(f)
