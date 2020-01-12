N = int(input())
a = [int(n) for n in input().split()]
c = 0
idx = {i:[] for i in range(1,N+1)}
for i,v in enumerate(a):
    idx[v].append(i)
print(idx)
flg = -1
l = 0
for j in range(1, N):
    if not idx[j]:
        print(flg)
        break
    else:
        for k in idx[j]:
            ok = False
            if l < k:
                l = k
                c += 1
                flg = N - c
                ok = True
                break
        if not ok:
            print(flg)
            break
print(flg)
