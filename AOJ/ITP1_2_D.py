W, H, x, y, r = [int(n) for n in input().split()]
print('Yes' if 0<=(x-r) and 0<=(y-r) and (x+r)<=W and (y+r)<=H else 'No')
