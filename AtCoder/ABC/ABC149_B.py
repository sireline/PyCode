A, B, K = [int(n) for n in input().split()]
if K>A:
    K -= A
    if K>B:
        print(0,0)
    else:
        print(0, B-K)
else:
    print(A-K,B)
