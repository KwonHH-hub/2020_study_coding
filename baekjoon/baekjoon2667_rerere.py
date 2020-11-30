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

            # 방법 1
            # if current[0] >= 1 and graph[current[1]][current[0] - 1] == '1' and (current[1], current[0] - 1) not in queue:
            #     queue.append((current[0] - 1, current[1]))
            #
            # if current[0] <= 6 and graph[current[1]][current[0] + 1] == '1' and (current[1], current[0] + 1) not in queue:
            #     queue.append((current[0] + 1, current[1]))
            #
            # if  current[1] >= 1 and graph[current[1] - 1][current[0]] == '1' and (current[1] - 1, current[0]) not in queue:
            #     queue.append((current[0], current[1] - 1))
            #
            # if  current[1] <= 6 and graph[current[1] + 1][current[0]] == '1' and (current[1] + 1, current[0]) not in queue:
            #     queue.append((current[0], current[1] + 1))

            # 방법 2
            # 방법 1, 2 중에서 뭐가 더 최적인지 모르겠음
            if current[0] >= 1 and graph[current[1]][current[0] - 1] == '1':
                if (current[1], current[0] - 1) not in queue:
                    queue.append((current[0] - 1, current[1]))

            if current[0] <= 6 and graph[current[1]][current[0] + 1] == '1':
                if (current[1], current[0] + 1) not in queue:
                    queue.append((current[0] + 1, current[1]))

            if  current[1] >= 1 and graph[current[1] - 1][current[0]] == '1':
                if (current[1] - 1, current[0]) not in queue:
                    queue.append((current[0], current[1] - 1))

            if  current[1] <= 6 and graph[current[1] + 1][current[0]] == '1':
                if (current[1] + 1, current[0]) not in queue:
                    queue.append((current[0], current[1] + 1))

    return count

size = int(input())
graph = [list('n'*(size+1))]
answer = []

for _ in range(size):
    graph.append(list('n' + sys.stdin.readline().strip()))

for y in range(1, size+1):
    for x in range(1, size+1):
        if graph[y][x] == '1':
            answer.append(bfs(x, y))

answer.sort()
print(len(answer))
for a in answer:
    print(a)

