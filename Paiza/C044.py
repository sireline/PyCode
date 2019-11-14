N = int(input())
O = {'paper': 0, 'rock': 1, 'scissors': 2}
a = []
for i in range(N):
    a.append(input())
hands = set(a)
l = len(hands)
if l==1 or l==3:
    print('draw')
else:
    result = (hands[0]-hands[1]+3) % 3
    if result == 2:
        print(O[hands[0]])
    else:
        print(O[hands[1]])
