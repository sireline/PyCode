N = int(input())
o = {}
for _ in range(N):
    o.setdefault(input(), "")
print(len(set(o)))
