d = [2,5,9,3,7,2,9,3,8,2,3]

mc = len(d) - 1

INF = float('inf')

C = [[INF for j in range(mc+1)] for i in range(mc+1)]
P = [[0 for j in range(mc+1)] for i in range(mc+1)]

for i in range(1, mc+1):
    C[i][i] = 0

for sps in range(2, mc+1):  # sub_problem_size
    spc = mc - sps + 1      # sub_problem_count
    for beg in range(1, spc+1):
        end = beg + sps - 1  # 예를 들면 sps=3, beg=4, end=6
        for k in range(beg, end):
            cost = C[beg][k] + C[k+1][end] + d[beg-1]*d[k]*d[end]
            if cost < C[beg][end]:
                C[beg][end] = cost
                P[beg][end] = k

def path(i, j):
    if i == j:
        return f'A{i}'
    k = P[i][j]
    a = path(i, k)
    b = path(k+1, j)
    return f'({a}x{b})'

print(path(1, mc), C[1][mc])