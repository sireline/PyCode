N = int(input())
o = {}
c = 0
for _ in range(N):
    k = "".join(sorted(input()))
    if k not in o:
        o[k] = 0
    else:
        o[k] += 1
        c += o[k]
print(c)
