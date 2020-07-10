H, W, K = [int(n) for n in input().split()]
A = ""
ans = 0
for i in range(H):
    A += input()
print(f'A: {A}')
if A.count('#') == K:
    print(1)
    exit()
for i in range(H):
    R = list(A)
    for j in range(i*W, i*W+W):
        R[j] = '.'
#    print(R)
    if R.count('#') == K:
        ans += 1
        print(f'ANS-R: {R}')
for i in range(W):
    C = list(A)
    for j in range(i, len(A), W):
        C[j] = '.'
#    print(C)
    if C.count('#') == K:
        ans += 1
        print(f'ANS-C: {C}')
for i in range(H):
    RC = list(A)
    print(f'RC: {RC}')
    for j in range(i*W, i*W+W):
        RC[j] = '.'
    print(f'RC-after: {RC}')
    if RC.count('#') >= 2:
        CR = RC[::]
        for k in range(W):
            for l in range(k, len(CR), W):
                CR[l] = '.'
            print(f'CR: {CR}')
            if CR.count('#') == K:
                ans += 1
                print(f'ANS-CR: {CR}')
print(ans)
