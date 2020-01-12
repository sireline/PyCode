n, m = [int(n) for n in input().split()]
s = input().split()
t = input().split()
q = int(input())
for _ in range(q):
    idx = int(input())
    print(s[idx%n-1]+t[idx%m-1])
