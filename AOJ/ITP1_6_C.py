N = int(input())
bfr = [[[0]*10 for i in range(3)] for j in range(4)]
for i in range(N):
    b, f, r, v = [int(n) for n in input().split()]
    bfr[b-1][f-1][r-1] += v
c = 0
for B in bfr:
    for F in B:
        print(' '.join([str(c) for c in F]).rjust(20))
#        print('{:>20}'.format(' '.join([str(c) for c in F])))
    c += 1
    if c < 4:
        print('####################')
