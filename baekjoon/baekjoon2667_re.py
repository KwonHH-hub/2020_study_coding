import sys

# dfs 하는 함수를 선언
def find(c, r, size):
    global visited
    global graph
    global count
    global ans

    if not (c,r) in visited:
        visited.append((c,r))

    if c + 1 == size:
        pass
    else:
        if graph[c+1][r] == '1':
            if not ((c+1, r) in visited or (c+1,r) in will_visit):
                will_visit.append((c+1, r))

    if r + 1 == size:
        pass
    else:
        if graph[c][r + 1] == '1':
            if not ((c, r+1) in visited or (c, r+1) in will_visit):
                will_visit.append((c, r+1))

    if c - 1 < 0:
        pass
    else:
        if graph[c-1][r] == '1':
            if not ((c-1, r) in visited or (c-1, r) in will_visit):
                will_visit.append((c-1, r))

    if r - 1 < 0:
        pass
    else:
        if graph[c][r-1] == '1':
            if not ((c, r-1) in visited or (c, r-1) in will_visit):
                will_visit.append((c, r-1))



    # print('in find function : will visit = ? ', will_visit)
    while will_visit:
        current = will_visit.pop()
        count += 1
        find(current[0], current[1], size)

    if not count == 0:
        ans.append(count + 1)
    count = 0


count = 0
visited = []
will_visit = []
ans = []

# 행,열의 크기(size) 와 전체 지도(graph)를 입력받음
graph = []
size = int(input())
for _ in range(size):
    graph.append(sys.stdin.readline().strip())

for col in range(size):
    for row in range(size):
        if graph[col][row] == '1':
            if (col, row) in visited:
                pass
            else:
                find(col, row, size)
        # print(visited)
answer = sorted(ans)
print(len(ans))
for a in answer:
    print(a)
