a, b = [c for c in input().split()]
print(sorted([a*int(b), b*int(a)])[0])
