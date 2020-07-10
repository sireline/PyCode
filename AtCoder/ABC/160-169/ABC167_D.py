N, K = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]
o = {i:0 for i in range(1, N+1)}
idx = 1
O = []
while True:
    if o[idx]==0:
        o[idx] = 1
        O.append(idx)
        idx = A[idx-1]
    else:
        c = K-sum(o.values())
        print(c, o)
        print(O)
        IDX = A.index(idx)
        print(f'{A}, IDX: {A.index(idx)}')
        l = len(O[A[IDX]-1:])
        print(f'LEN: {l}')
        print(O[c % l])
        break
