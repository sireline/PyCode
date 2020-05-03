N = int(input())
A = [int(n) for n in input().split() if int(n)%2==0]
print('APPROVED' if all([1  if n%3==0 or n%5==0 else 0 for n in A]) else 'DENIED')
