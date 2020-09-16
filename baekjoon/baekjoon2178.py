# 실패

def dir(pose, dir):
    if pose[0] == 6 or pose[1] == 4:
        return
    else:
        return [pose[0]+dir[0], pose[1]+dir[1]]


def find(start, check, graph):
    graph[start[0]][start[1]] = 2
    to_x = [dir(start,dx)[0],dir(start,dx)[1]]
    to_y = [dir(start, dy)[0], dir(start, dy)[1]]
    to_xy = [dir(start, dxdy)[0], dir(start, dxdy)[1]]
    if graph[to_x[0]][to_x[1]] == 1:
        check.append([to_x[0],to_x[1]])
    if graph[to_y[0]][to_y[1]] == 1:
        check.append([to_y[0],to_y[1]])
    if graph[to_xy[0]][to_xy[1]] == 1:
        check.append([to_xy[0],to_xy[1]])
    start = c[0]
    check.pop(0)
    return start,


dx = [1, 0]
dy = [0, 1]
dxdy = [1, 1]
c = []
# graph = []
start = [0,0]
# n, m = map(int, input().split(' '))
n, m = 4,6
print(n,m)
# graph = [list(map(int, input())) for _ in range(n)]
graph = [
        [1,0,1,1,1,1],
        [1,0,1,0,1,0],
        [1,0,1,0,1,1],
        [1,1,1,0,1,1]
]

print(graph)
s = find(start,c,graph)
k = find(s,c,graph)
find(k,c,graph)

# for _ in range(15):
#     s = find(s,c,graph)
print(graph)