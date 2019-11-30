from datetime import datetime
import random
import bisect

for i in range(1000):
    for j in range(1000):
        if i+j==3:
            print(3)
            exit()

K = [random.randint(1, 100) for _ in range(1000)]
M = int(input())
print(K)
K.sort()
print(K)

print(f'START: {datetime.now()}')

print(M in K)

print(f'END: {datetime.now()}')



print(f'START: {datetime.now()}')

print(bisect.bisect(K,M))

print(f'END: {datetime.now()}')
