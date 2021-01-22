N = int(input())
C = list(input())
CC = C[::-1]
RC = C.count('W')
WC = C.count('R')
ans = min(WC, RC)
XC = 0
if ans==0:
    print(0)
else:
    l = 0
    r = 0
    while ans > XC:
        print(C[l:N-r])
        l = C.index('W')
        r = CC.index('R')
        print(l,r)
        if l > N-1-r:
            ans = min(XC, ans)
            break
        C[l],C[N-1-r] = C[N-1-r],C[l]
        CC[r],CC[N-l-1] = CC[N-l-1],CC[r]
        XC += 1
    print(ans)
    