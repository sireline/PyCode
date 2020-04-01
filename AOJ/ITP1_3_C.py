while True:
    ans = sorted([int(n) for n in input().split()])
    if sum(ans) == 0:
        break
    print(*ans)
