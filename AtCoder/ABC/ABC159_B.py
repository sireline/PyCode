S = list(input())
ans = 'No'
N = len(S)
if S==S[::-1]:
    if S[0:(N-1)//2] == S[0:(N-1)//2][::-1]:
        if S[(N+3)//2-1:] == S[(N+3)//2-1:][::-1]:
            ans ='Yes'
print(ans)
