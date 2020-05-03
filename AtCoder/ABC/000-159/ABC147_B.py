S = input()
RS = S[::-1]
c = 0
for i in range(len(S)//2):
    if S[i] != RS[i]:
        c += 1
print(c)
