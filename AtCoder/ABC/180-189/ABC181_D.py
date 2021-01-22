from itertools import permutations

S = [n for n in list(input())]
for p in permutations(S, len(S)):
    ans = "".join(c for c in p)
    if int(ans)%8==0:
        print('Yes')
        exit()
print('No')
