from itertools import product
from math import gcd

K = int(input())
print(sum([gcd(a,gcd(b,c)) for a,b,c in [i for i in product(range(1, K+1), repeat=3)]])) 
