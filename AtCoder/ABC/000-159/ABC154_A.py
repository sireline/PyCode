S, T = input().split()
A, B = [int(n) for n in input().split()]
ans = {S:A, T:B}
U = input()
ans[U] -= 1
print(ans[S], ans[T])
