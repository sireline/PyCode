A, B = input().split()
print(max(sum([int(x) for x in list(A)]), sum([int(x) for x in list(B)])))
