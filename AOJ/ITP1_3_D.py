ans = 0
a, b, c = [int(n) for n in input().split()]
for n in range(a, b+1):
    if (c/n).is_integer():
        ans += 1
print(ans)
