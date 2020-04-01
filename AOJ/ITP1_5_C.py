while True:
    H, W = [int(n) for n in input().split()]
    if H == 0 and W == 0:
        break
    for i in range(H):
        d, r = divmod(W, 2)
        if i%2 == 0:
            print('#.'*d+'#'*r)
        else:
            print('.#'*d+'.'*r)
    print()
