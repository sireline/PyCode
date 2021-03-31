S = list(input())
ans = 'Yes'
for i, s in enumerate(S):
    if i%2:
        if s == s.lower():
            ans = 'No'
            break
    else:
        if s == s.upper():
            ans = 'No'
            break
print(ans)