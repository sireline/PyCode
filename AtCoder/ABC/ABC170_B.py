from itertools import combinations_with_replacement

X, Y = [int(n) for n in input().split()]
ans = 'No'
for i in range(X+1):
    for j in range(X+1):
        if i+j == X and 2*i+4*j == Y:
            ans = 'Yes'
            break
print(ans)
