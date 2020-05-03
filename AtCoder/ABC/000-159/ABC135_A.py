A, B = [int(n) for n in input().split()]
print('IMPOSSIBLE' if (A+B)%2 else (A+B)//2)
