N, M = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]
O = [0]*N
for i in A:
    ans = -1
    for j,n in enumerate(O):
        #print(i,j,n)
        if n < i:
            O[j] = i
            ans = j+1
            break
        #print(O)
    print(ans)
