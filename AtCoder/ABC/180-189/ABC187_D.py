import heapq

N = int(input())
Asum = 0
Bsum = 0
A = []
B = []
for i in range(N):
    a, b = [-int(n) for n in input().split()]
    Asum += (-a)
    heapq.heappush(A, (a, i))
    heapq.heappush(B, (b, i))
print(A)
print(B)
