coords = [
(620, 332), (784, 623), (182, 555), (1413, 451), (1092, 660), (30, 217), (525, 148), (1311, 887), (1228, 353), (54, 68),
(1155, 838), (467, 563), (86, 535), (32, 630), (739, 766), (1386, 16), (1565, 828), (868, 264), (1301, 786), (883, 415),
(479, 534), (1101, 35), (671, 405), (1478, 230), (1343, 834), (647, 97), (972, 447), (327, 334), (716, 151), (233, 411),
(486, 431), (1017, 381), (329, 830), (1286, 739), (1528, 248),(216, 294), (1306, 540), (204, 715), (77, 120), (97, 178),
(809, 28), (354, 205), (123, 551), (248, 828), (888, 139), (594, 494), (576, 702), (64, 218)
]

def dist(a,b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    # d = 1 #???

def dist_sq(a,b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    #d = 2 #???

def brute_force(arr,i1,i2):
    md = float('inf')
    s,e = -1, -1
    for x in range(i1-i2):
        for y in range(x+1-i2):
            d = dist(arr[x],arr[y])
            if d <md:
                md =d
                s, e = x, y

    return s,e,md

def dnc(arr,i1,i2) :
    size = i2 - i1 + 1
    if size <=1: return -1, -1, float('inf')
    if size ==2: return i1,i2,dist([i1],[i2])
    if size ==3: return brute_force(arr,i1,i2)
    mid = (i1 + i2) //2
    mid_x = arr[mid][0]
    s1, e1, d1 = dnc(arr,i1,mid)
    s2, e2, d2 = dnc(arr,mid +1, i2)

    if d1 < d2:
        d = d1
        s, e = s1, e1
    else:
        d = d2
        s, e = s2, e2

    # d 결정.

    # x좌표 : 중간점 x좌표 - d ~ 중간점 x좌표 + d
    # index1 : x좌표가 중간점 x좌표-d 이상인 점들중 가장 왼쪽 index
    # index1 : x좌표가 중간점 x좌표+d 이상인 점들중 가장 오른쪽 index
    strip = [arr[i] for i in range(i1,i2+1) if abs(arr[i][0] - mid_x)<d]
    strip.sort(key=lambda point: point[1])

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < d:
            d_strip = dist(strip[i], strip[j])
            if d_strip < d:
                d = d_strip
                s, e = arr.index(strip[i]), arr.index(strip[j])
            j += 1

    return s, e, d

print(coords)
coords.sort(key = lambda t:t[0])
x_sorted = [(coords[i][0], coords[i][1], i) for i in range(len(coords))]
print('----------------------------------------------x sorted ----------------------------------------------')
print(x_sorted)
y_sorted = sorted(x_sorted, key=lambda t:t[1])
print('----------------------------------------------y sorted ----------------------------------------------')
print(y_sorted)

# s,e,d = brute_force(coords, 0, len(coords)-1)
s,e,d = dnc(coords, 0, len(coords)-1)

# print(f'[{s}]{coords[s]} - [{e}]{coords[e]}, {d}')
# s,e,d = brute_force(coords, 0, len(coords)-1)
# s,e,d = dnc(coords,0,len(coords)-1)

print(f'[{s}]{coords[s]} - [{e}]{coords[e]}, d= {d}')