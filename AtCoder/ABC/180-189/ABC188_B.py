N = int(input())
ans = []
A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]
for i in range(N):
    ans.append(A[i]*B[i])
print('Yes' if sum(ans)==0 else 'No')
