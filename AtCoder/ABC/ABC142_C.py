N = int(input())
A = ["0"]*N
for a,i in zip(input().split(), range(1,N+1)):
    A[(int(a)-1)] = str(i)
print(" ".join(A))
