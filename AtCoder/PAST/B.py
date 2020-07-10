N, M, Q = [int(n) for n in input().split()]
q = {k:[] for k in range(1, M+1)}
man = {k:[0]*M for k in range(1, N+1)}

for i in range(Q):
    Lines = [int(n) for n in input().split()]
    if Lines[0]==1:
        print(sum(man[Lines[1]]))
    else:
        q[Lines[2]].append(Lines[1])
        point = N - len(q[Lines[2]])
        for i in q[Lines[2]]:
            man[i][Lines[2]-1] = point
