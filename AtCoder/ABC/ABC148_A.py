A = int(input())
B = int(input())
print([x for x in [1,2,3] if not x in [A, B]][0])