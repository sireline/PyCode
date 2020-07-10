ans ={'AC':0, 'WA':0, 'TLE':0, 'RE':0}
N = int(input())
for _ in range(N):
    k = input()
    c = ans.setdefault(k)
    ans[k] += 1
for k,v in ans.items():
    print(f'{k} x {v}')
