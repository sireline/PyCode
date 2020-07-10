n = int(input())
ans = 0

def eratos(n):
    p = [2]
    l = list(range(3, 100, 2))
    while l[0] < int(100**0.5)+1:
        p.append(l.pop(0))
        l = [x for x in l if x % p[-1]]
    return p + l

def is_primenumber(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True 

P = eratos(n)
X = []
while True:
    if n == 1:
        print(ans)
        break
    if is_primenumber(n):
        n /= n
        ans += 1
    else:
        for i in range(1, 100):
            print(f'N: {n}')
            print(f'I: {i}')
            for p in P:
                z = p**i
                if n%z==0 and z not in X:
                    print(f'Z: {z}')
                    X.append(z)
                    n /= z
                    ans += 1
                    print(ans)
                    break
