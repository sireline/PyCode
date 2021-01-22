import math

K = int(input())
ans = -1
dp = [7]
if K%2==0:
    ans = -1
else:
    i = math.log10(K)
    x = dp[0]*10**i+dp[i-1]
    print(i, x)
#    while True:
#        if x%K==0:
#            ans = i+1
#            break
#        dp.append(x)
#        i += 1
#print(ans)
