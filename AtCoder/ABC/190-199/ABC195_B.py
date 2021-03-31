A, B, W = [int(n) for n in input().split()]
W *= 1000
l, lr = divmod(W, B)
r, rr = divmod(W, A)
if lr == 0 == rr:
    print(l, r)
    exit()
if l+1 <= r:
    print(l+1, r)
else:
    print('UNSATISFIABLE')