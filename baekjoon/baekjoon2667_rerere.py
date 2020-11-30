import sys
from collections import deque

def bfs(x, y):
    global graph

    queue = deque()
    queue.append((x,y))
    count = 0

    while queue:
        current = queue.popleft()
        if graph[current[1]][current[0]] == '1':
            graph[current[1]][current[0]] = '2'
            count += 1

            if graph[current[1]][current[0] - 1] == '1' and (current[1], current[0] - 1) not in queue:
                # relation += 1
                queue.append((current[1], current[0] - 1))
            if graph[current[1] - 1][current[0]] == '1' and (current[1] - 1, current[0]) not in queue:
                # relation += 1
                queue.append((current[1] - 1, current[0]))
            if graph[current[1]][current[0] + 1] == '1' and (current[1], current[0] + 1) not in queue:
                # relation += 1
                queue.append((current[1], current[0] + 1))
            if graph[current[1] + 1][current[0]] == '1' and (current[1] + 1, current[0]) not in queue:
                # relation += 1
                queue.append((current[1] + 1, current[0]))
        print('count ', count)
        print('graph ', graph)


# def pointer (y, x):
#     return [(y-1,x), (y,x-1), (y, x+1), (y+1, x)]

size = int(sys.stdin.readline().strip())
graph = [list('n'*(size+1))]

for _ in range(size):
    graph.append(list('n' + sys.stdin.readline().strip()))
print(size)
print('type of size : ', type(size))
print(graph)
print('type of graph : ', type(graph))

for y in range(1, size):
    for x in range(1, size):
        if graph[y][x] == '1':
            # graph[y][x] = '2'
            bfs(x, y)

