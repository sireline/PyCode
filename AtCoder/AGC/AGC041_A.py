N, A, B = [int(n) for n in input().split()]
if (B-A)%2==0:
    print((B-A)//2)
else:
    print(A+(B-A)//2 if (A-1) < (N-B) else (N-B+1)+(B-A)//2)
