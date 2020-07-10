X = int(input())
f = False
i = 0
while i < 3000:
    if f:
        break
    j = i-1
    while X > (i**5-j**5):
        if X == (i**5-j**5):
            print(i, j)
            f = True
            break
        j -= 1
    i += 1
