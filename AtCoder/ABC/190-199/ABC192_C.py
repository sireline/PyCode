def g1(x):
    X = list(x)
    print(X)
    return "".join(sorted(X, reverse=True))

def g2(x):
#    return "".join(sorted([c for c in list(x) if c != '0']))
    return "".join(sorted(list(x)))

def f(x):
    return str(int(g1(x)) - int(g2(x)))

N, K = input().split()
K = int(K)
a = [N]
for i in range(K):
    a.append(f(a[i]))
print(a[K])