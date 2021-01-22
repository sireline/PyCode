from decimal import Decimal
import math

X, Y, A, B = [Decimal(n) for n in input().split()]
c = 0
n = int(math.log(B,A))
