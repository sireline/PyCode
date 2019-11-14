import math

A,　B,　C,　D = [int(n) for n in input().split()]
ans = 1/2　*　(abs(A*D-B*C))
print(math.ceil(ans))
