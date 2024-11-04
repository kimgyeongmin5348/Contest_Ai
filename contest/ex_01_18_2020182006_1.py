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
parent = list(range(num_vertex))

roots = []

mst = []

def append(s, e, w):
    if s <= e:
        mst.append((s,e,w))
    else:
        mst.append((e,s,w))
    mst.sort(key=lambda e:e[0]*1000+e[1])
def spanning():
    return len(mst) >= num_vertex - 1
def onSameTree(u, v):
    return getRoot(u) == getRoot(v)
def getRoot(v):
    if parent[v] != v:
        parent[v] = getRoot(parent[v])
    return parent[v]
def connect(u, v):
    parent[getRoot(u)] = getRoot(v)

edges.sort(key=lambda e: e[2])

for s,e,w in edges:
    if spanning(): break
    if onSameTree(s, e): continue

    mst.append((s, e, w))
    connect(s, e)

print(mst)

