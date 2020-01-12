N = int(input())
s = []
t = []
for i in range(N):
    st = [c for c in input().split()]
    s.append(st[0])
    t.append(int(st[1]))
X = input()
print(sum(t[s.index(X)+1:]))
