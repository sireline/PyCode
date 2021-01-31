A, B, C = [int(n) for n in input().split()]
AB = [A, B]
turn = C
def eat(turn):
    global AB
    AB[turn] -= 1
    return not turn
while AB[0]>=0 and AB[1]>=0:
    turn = eat(turn)
print('Takahashi' if AB[0]>=0 else 'Aoki')