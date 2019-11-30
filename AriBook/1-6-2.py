L = int(input())
N = int(input())
X = [int(n) for n in input().split()]
print(max([x if x <= L/2 else L-x for x in X]), max([L-x if x <= L/2 else x for x in X]))
