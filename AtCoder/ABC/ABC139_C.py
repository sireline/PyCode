N=int(input())
H=[int(n) for n in input().split()]
c=0
m=0
for i in range(1, N):
    if H[-(i+1)] >= H[-i]:
      c += 1
      if m<c:
          m = c
    else:
      c=0
print(m)
