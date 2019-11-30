N = int(input())
S = input()
AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for c in S:
    print(AZ[(AZ.index(c)+N) % len(AZ)], end="")
