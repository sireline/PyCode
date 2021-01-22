N = int(input())
X = [int(n) for n in input().split()]
print(sum([abs(x) for x in X]))
print('{:.20f}'.format(sum([abs(x)**2 for x in X])**0.5))
print(max([abs(x) for x in X]))
