N = int(input())
B = [int(n) for n in input().split()][::-1]
print(sum([B[0],B[N-2]]+[min(B[i-1],B[i]) for i in range(1,N-1)]))
