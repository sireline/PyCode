N, K = [int(n) for n in input().split()]
H = [int(h) for h in input().split()]
print(len([x for x in H if x>=K]))
