N = int(input())
A = [int(n) for n in input().split()]
d = 2**N//2
l = max(A[:d])
r = max(A[d:])
ans_idx = min(l, r)
print(A.index(ans_idx)+1)
