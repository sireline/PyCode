S = input()
c = 0
for l in range(len(S)-3):
    for r in range(l+4, len(S)+1):
        if int(S[l:r])%2019 == 0:
            print(l, r)
            c += 1
print(c)
