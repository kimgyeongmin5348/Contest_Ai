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



print('Using Maximul Matching')

n_edges = len(edges)

# build adj set from edges
from collections import defaultdict
import random
random.seed('hello')
g = defaultdict(set)
for i in range(len(edges)):
    u, v, w = edges[i]
    g[u].add(v)
    g[v].add(u)

# 구하려는 Set Cover 해 정점들
vc = set()

import random
vertices = list(range(num_vertex))
covered_edge = 0
while covered_edge < n_edges:
    random_index = random.randint(0, len(vertices) - 1)
    u = vertices.pop(random_index)  # randomly select from vertices
    if not g[u]:
        continue  # 이 점 주위에 연결된것이 없다면 (모두 지워졌다면) 넘어간다
    v = next(iter(g[u]))  # u 에 연결된 점 하나 뽑아오기
    vertices.remove(v)  # v 도 vertices 에서 제거

    # 모든 점 k 에 대해 u~k, v~k 간선을 삭제한다.
    for n in [u, v]:
        vc.add(n)
        for k in list(g[n]):  # 모든 점 k 에 대하여
            if k in g[n]:  # n 에서 k 로 가는 선이 살아있다면 (안 지워졌다면)
                g[k].remove(n)  # 그 선은 지운다
                g[n].remove(k)
                covered_edge += 1  # 선의 갯수 +1

print(len(vc), vc)
