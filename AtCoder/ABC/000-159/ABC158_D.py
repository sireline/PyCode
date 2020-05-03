S = input()
Q = int(input())

for i in range(Q):
    t = input()
    if t[0] == '1':
        S = S[::-1]
        continue
    if t[2] == '1':
        S = t[4] + S
    else:
        S = S + t[4]
print(S)
