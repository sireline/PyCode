A, B, C = [int(n) for n in input().split()]
T = sum([A, B, C])
N = 100
print((N-A)*(A/T)+(N-B)*(B/T)+(N-C)*(C/T))