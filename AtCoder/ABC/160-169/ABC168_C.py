import math

A, B, H, M = [int(n) for n in input().split()]
rad = math.radians(abs(H*30.0-M*6.0))
print((A**2.0+B**2.0-2*A*B*math.cos(rad))**0.5)
