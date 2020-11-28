import sys

def find(col, row, size):
    global graph
    global count
    if graph[col][row] == '1':
        will_visit.append((col, row))
        count += 1
        graph[col][row] = '2'
    size_ = size

    if col-1 > 0  and graph[col-1][row] == '1':
        find(col-1, row, size_)

    elif row-1 >= 0 and graph[col][row-1] == '1':
        find(col, row-1, size_)

    elif row+1 < size_ and graph[col][row+1] == '1':
        find(col, row+1, size_)

    elif col+1 <= size_ and graph[col+1][row] == '1':
        find(col+1, row, size_)

    if will_visit:
        current = will_visit.pop()
        find(current[0], current[1], size_)


count = 0
will_visit = []
ans = []

# 행,열의 크기(size) 와 전체 지도(graph)를 입력받음
graph = [[]]
size = int(input())

for _ in range(size):
    graph[0].append('0')
    ss = []
    for s in sys.stdin.readline().strip():
        ss.append(s)
    graph.append(ss)
# print(graph)

for col in range(1, size+1):
    for row in range(size):
        if graph[col][row] == '1':
            find(col, row, size)
            ans.append(count)
            count = 0

answer = sorted(ans)
print(len(answer))
for a in answer:
    print(a)