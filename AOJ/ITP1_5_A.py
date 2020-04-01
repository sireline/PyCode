while True:
    H, W = [int(n) for n in input().split()]
    if H == 0 and W == 0:
        break
    for i in range(H):
        print('#'*W)
    print()
