import math

a, p = [int(n) for n in input().split(" ")]
print(math.floor((a/100+1.0) * p))
