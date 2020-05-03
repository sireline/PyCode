N = int(input())
P = (int(n) for n in input().split())
Q = (int(n) for n in input().split())

def kaijyou(n):
    if n <= 1: return 1
    return n * kaijyou(n-1)

def pos(n):

l = [n for n in range(1,N+1)]

a = sum([l.index(p)*kaijyou(N-i) for i,p in enumerate(P, start=1)])
b = sum([l.index(q)*kaijyou(N-i) for i,q in enumerate(Q, start=1)])
print(abs(a-b))
