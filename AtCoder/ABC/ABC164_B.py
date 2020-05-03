A, B, C, D = [int(n) for n in input().split()]
while True:
    C -= B
    if C<=0:
        break
    A -= D
    if A<=0:
        break
print('Yes' if A>C else 'No')
