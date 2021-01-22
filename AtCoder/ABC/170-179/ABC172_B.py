S = input()
T = input()
i = 0
for s, t in zip(S, T):
    if s!=t:
        i += 1
print(i)
