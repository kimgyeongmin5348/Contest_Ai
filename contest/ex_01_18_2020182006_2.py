import heapq

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

graph = {i: [] for i in range(num_vertex)}
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))


def prim(start):
    visited = set()
    mst = []
    min_heap = [(0, start, start)]

    while min_heap and len(visited) < num_vertex:
        w, u, prev = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        if u != prev:
            mst.append((prev, u, w))

        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (weight, v, u))

    return mst


result = prim(8)
print(result)
