S = input()
T = input()
ans = len(T)
if len(T)==len(S):
    loop = 1
else:
    loop = len(S)-len(T)
for i in range(loop):
    diff = 0
    for s, t in zip(S[i:i+len(T)], T):
        if s!=t:
            diff += 1
    ans = min(ans, diff)
print(ans)
