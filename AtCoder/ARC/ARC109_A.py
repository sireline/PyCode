a, b, x, y = [int(n) for n in input().split()]
if a==b:
    print(x)
elif a>b:
    print((a-b)*x)
else:
    print(min(2*x, y)*(b-a)+x)
