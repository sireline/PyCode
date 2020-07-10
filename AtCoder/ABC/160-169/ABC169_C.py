from decimal import Decimal

A, B = [n for n in input().split()]
print(int(Decimal(A) * Decimal(B)))
