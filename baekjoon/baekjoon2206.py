import sys
from collections import deque
dx = [0,1,-1,0]
dy = [1,0,0,-1]

def find(n, m, visited):
    global node
    q = deque()

    limit_x = len(node[0])
    limit_y = len(node)
    q.append((n,m))
    count = 0
    current_y = 0

    while q:
        current = q.popleft()
        if current_y > current[0] :
            continue
        count += 1
        current_x = current[1]
        current_y = current[0]


        if visited[current_y][current_x] == 0 and node[current_y][current_x] == '0':
            visited[current_y][current_x] = 1

        for d in range(len(dx)):
            ambient_x = current_x + dx[d]
            ambient_y = current_y + dy[d]

            if ambient_x >= 0 and ambient_y >= 0 and ambient_x < limit_x and ambient_y < limit_y:
                if visited[ambient_y][ambient_x] == 0 and node[ambient_y][ambient_x] == '0':

                    q.append((ambient_y, ambient_x))

    if current_x == limit_x - 1 and current_y == limit_y - 1:
        return count
    else:
        return -1



n, m = map(int, input().split())
node = []
answer = []
count = 0

for _ in range(n):
    temp = sys.stdin.readline().strip()
    node.append(temp)

for nn in range(n):
    nd = node[nn]
    for mm in range(m):
        if nd[mm] == '1':
            visited = [[0] * (m) for _ in range(n)]
            node[nn] = nd[:mm] +'0'+ nd[mm+1:]
            answer.append(find(0,0,visited))
            node[nn] = nd[:mm] + '1' + nd[mm + 1:]

answer = list(set(answer))
answer.sort()
answer.remove(-1)

if answer:
    print(answer[0])
else:
    print(-1)
