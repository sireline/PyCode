N = int(input())
A = [int(n) for n in input().split()]
print('YES' if len(set(A))==len(A) else 'NO')
