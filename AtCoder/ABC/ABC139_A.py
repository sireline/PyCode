Y=input()
S=input()
print(sum([1 for a,b in zip(Y,S) if a==b]))
