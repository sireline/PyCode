H =int(input())
c = 0
while H:
    H = H >> 1
    c += 1
print(2**c-1)
