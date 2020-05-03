from collections import deque

R, C = [int(n) for n in input().split()]
sy, sx = [int(n)-1 for n in input().split()]
gy, gx = [int(n)-1 for n in input().split()]
p=[list(input()) for _ in [0]*R]

def draw():
    global C,p
    print("*"*20)
    print("  ", end="")
    print("".join([str(i) for i in range(C)]))
    for idx,r in enumerate(p):
        print(f"{idx} ", end="")
        print("".join([str(c) for c in r]))
    print("*"*20)

print(f'START: ({sy},{sx}) => GOAL: ({gy},{gx})')
draw()
p[sy][sx] = 0
d=[(1,0), (-1,0), (0,1), (0,-1)]
q=deque([[sy, sx]])
while q:
    print(f"Q: {q}")
    x, y = q.popleft()
    print(f"P(x,y): ({x},{y})=>{p[x][y]}")
    for dx, dy in d:
        if p[x+dx][y+dy] == '.':
            p[x+dx][y+dy] = p[x][y]+1
            q.append([x+dx, y+dy])
    draw()
print("*"*20)
print(p[gy][gx])
