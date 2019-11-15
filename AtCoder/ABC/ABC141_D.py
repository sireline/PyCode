import heapq

N, M = [int(n) for n in input().split()]
A = [-int(n) for n in input().split()]
heapq.heapify(A)
[heapq.heappush(A, -(-heapq.heappop(A)//2)) for _ in range(M)]   
print(-sum(A))
