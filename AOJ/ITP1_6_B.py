n = int(input())
R = ['S', 'H', 'C', 'D']
T = {'S': [True]*13, 'H': [True]*13, 'C': [True]*13, 'D': [True]*13}
for i in range(n):
    M, N = input().split()
    T[M][int(N)-1] = False
for r in R:
    for j, a in enumerate(T[r], 1):
        if a:
            print(r, j)
