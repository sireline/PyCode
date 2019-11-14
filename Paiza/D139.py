N = int(input())
O = [c for c in input().split()]
if O.count('G') == O.count('P'):
    print('Draw')
else:
    print('G' if O.count('G') < O.count('P') else 'P')
