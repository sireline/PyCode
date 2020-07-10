X = int(input())
n = 100
r = 0.01
c = 0
while True:
    if n >= X:
        break
    n = int(n+n*r)
    c += 1
print(c)
