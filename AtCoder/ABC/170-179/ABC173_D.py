N = int(input())
A = sorted([int(n) for n in input().split()], reverse=True)
print(sum(A[:N-1]))
