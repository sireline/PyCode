N = int(input())
f = False
for i in range(1, 10):
    for j in range(1, 10):
        if i*j == N:
            f = True
print('Yes' if f else 'No')
