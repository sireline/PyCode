import sys

print(sys.getrecursionlimit())
# 1000

sys.setrecursionlimit(10**9)
print(sys.getrecursionlimit())
# 1000000000
