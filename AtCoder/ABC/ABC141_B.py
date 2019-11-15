S = input()
O = set(S[::2])
E = set(S[1::2])
ans1 = [True if c in 'RUD' else False for c in O]
ans2 = [True if c in 'LUD' else False for c in E]
print('Yes' if False not in ans1 and False not in ans2 else 'No')
