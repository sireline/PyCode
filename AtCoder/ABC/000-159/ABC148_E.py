N = int(input())
x = [n for n in range(N, 0, -2) if n>=2]
y = 1
for i in x:
    y *= i
y = list(str(y))[::-1]
c = 0
for i in y:
    if i == "0":
        c += 1
    else:
        break
print(c)
