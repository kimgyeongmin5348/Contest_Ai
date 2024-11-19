d = [2,5,9,3,7,2,9,3,8,2,3]


mc = len(d) -1

INF = float('inf')

C = [[??? for ??? range(mc+1)]]
P =

for sps in range(2, mc+1): # sub_problem_size
    spc = ???   #sub_problem_count
    for beg in range(1, spc+1):
        end = ???  # 예를 들면 sps =3, sps = 4 , end = 6
        ???
        ???
        for k in range(beg, end):
            # 최소값 갱신

def path(i,j):
    if ???:
        return f'A{i}'
    ???
    return f'({a}x{b})'


print(path(1, mc), C[1][mc])