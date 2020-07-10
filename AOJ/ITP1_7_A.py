while True:
    f, m, r = [int(n) for n in input().split()]
    if f == m == r == -1:
        break
    if (f==-1 or m==-1) or (f+m < 30):
        ans = 'F'
    elif 30 <= f+m < 50:
        ans = 'D'
        if 50 <= r:
            ans = 'C'
    elif 50 <= f+m < 65:
        ans = 'C'
    elif 65 <= f+m < 80:
        ans = 'B'
    else:
        ans = 'A'
    print(ans)
