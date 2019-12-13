N = int(input())
A = [int(n) for n in input().split()]
Aset = set(A)
m = (10**9+7)
o = {}
ans = []
for a in A:
    o.setdefault(a, 0)
    o[a] += 1
for i in range(len(Aset)-1):
    for j in range(i+1, len(Aset)):
        ans.append((A[i]^A[j])*o[A[i]]*o[A[j]])
print(sum(ans)/m)
