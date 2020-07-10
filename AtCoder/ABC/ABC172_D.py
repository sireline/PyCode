import math
import heapq

N = int(input())

def f(N):
    if N<=2:
        return N
    ans = [1, N]
    heapq.heapify(ans)
    for i in range(2, math.ceil(N**0.5)+1):
        if N%i == 0:
            heapq.heappush(ans, i)
            if i*i != N:
                heapq.heappush(ans, N//i)
    return len(set(ans))

ans = 1
for i in range(2, N+1):
    ans += i*f(i)
print(ans)
