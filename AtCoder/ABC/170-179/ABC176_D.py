from collections import deque

def bfs(graph):
    search_queue = deque()
    search_queue += graph["you"]
    print(search_queue)
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
    return False

H, W = [int(n) for n in input().split()]
C = [int(n) for n in input().split()]
D = [int(n) for n in input().split()]
S = [[]]*W
for i in range(H):
    S[i].append([x for x in input().split()])
print(S)
print(abs(D[0]-C[0]), abs(D[1]-C[1]))