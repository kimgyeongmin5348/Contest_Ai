edges=[

    (0, 2, 267), (0, 10, 292), (0, 14, 162), (0, 17, 311), (0, 23, 281), 

    (1, 11, 331), (1, 19, 307), (1, 22, 395), (2, 6, 256), (2, 10, 319), 

    (2, 14, 111), (2, 16, 316), (2, 18, 405), (2, 20, 451), (2, 21, 415), 

    (2, 24, 488), (3, 8, 249), (3, 12, 438), (3, 15, 84), (4, 7, 445), 

    (4, 10, 53), (4, 16, 320), (4, 17, 135), (4, 20, 229), (4, 24, 298), 

    (5, 9, 367), (5, 13, 483), (5, 15, 261), (5, 19, 358), (6, 7, 109), 

    (6, 12, 358), (6, 14, 319), (6, 16, 456), (6, 18, 153), (6, 21, 465), 

    (7, 12, 440), (7, 13, 465), (7, 14, 210), (7, 23, 236), (8, 9, 106), 

    (10, 16, 285), (11, 13, 371), (11, 19, 53), (12, 13, 243), (12, 18, 364), 

    (12, 21, 395), (12, 22, 442), (13, 21, 170), (14, 18, 451), (14, 23, 318),

    (16, 17, 287), (16, 23, 325), (17, 24, 392), (19, 22, 146), (20, 24, 76)

]

num_vertex = 25

start = 12
## Prim

# Build Graph from Input Edge List
g = { s: dict() for s in range(num_vertex) }
for s,e,w in edges:
    g[s][e] = w
    g[e][s] = w

# Prepare Data Structures
from heapdict import heapdict
mst = []
D = heapdict()
D[start] = 0
origins = dict()
origins[start] = start
completed = set()
sum = 0
# Prim Main Loop
while D:
    to_vertex, weight = D.popitem()
    fr_vertex = origins[to_vertex]
    completed.add(to_vertex)
    if fr_vertex != to_vertex:
        mst.append((fr_vertex, to_vertex, weight))
        sum += weight
    for adj, adj_w in g[to_vertex].items():
        if adj in completed: continue       # 내륙이면 무시
        if adj in D and D[adj] <= adj_w: continue # 존재하고 기존게 싸면 무시
        D[adj] = adj_w
        origins[adj] = to_vertex

print(sum, mst)
# 4757 [(12, 13, 243), (13, 21, 170), (12, 6, 358), (6, 7, 109), (6, 18, 153), (7, 14, 210), (14, 2, 111), (14, 0, 162), 
# (7, 23, 236), (0, 10, 292), (10, 4, 53), (4, 17, 135), (4, 20, 229), (20, 24, 76), (10, 16, 285), (13, 11, 371), 
# (11, 19, 53), (19, 22, 146), (19, 1, 307), (19, 5, 358), (5, 15, 261), (15, 3, 84), (3, 8, 249), (8, 9, 106)]

## TSP
# Build Graph from MST
mg = { s: set() for s in range(num_vertex) }
for s,e,w in mst:
    mg[s].add(e)
    mg[e].add(s)

# Make Sequence
seq = [ start ]
current = start
while True:
    if current == start and not mg[start]: break
    for k in mg[current]:
        if k not in seq:
            visit = k
            break
    else:
        visit = list(mg[current])[0]
    mg[current].remove(visit)
    seq.append(visit)
    current = visit
print(seq)
# [12, 13, 11, 19, 1, 19, 5, 15, 3, 8, 9, 8, 3, 15, 5, 19, 22, 19, 11, 
# 13, 21, 13, 12, 6, 18, 6, 7, 23, 7, 14, 0, 10, 16, 10, 4, 17, 4, 20, 
# 24, 20, 4, 10, 0, 14, 2, 14, 7, 6, 12]

# Find Shortcut
visited = set()
index = 0
while index < len(seq):
    current = seq[index]
    if current in visited:
        seq.pop(index)
    else:
        visited.add(current)
        index += 1
seq.append(start)
print(seq)
# [12, 13, 11, 19, 1, 5, 15, 3, 8, 9, 22, 21, 6, 18, 7, 23, 14, 0, 10, 16, 4, 17, 20, 24, 2, 12]