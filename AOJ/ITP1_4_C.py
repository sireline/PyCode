OP = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: a // b
}
while True:
    a, op, b = [x for x in input().split()]
    if op == '?':
        break
    print(OP[op](int(a), int(b)))
