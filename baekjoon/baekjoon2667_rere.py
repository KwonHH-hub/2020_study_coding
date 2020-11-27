import sys

# dfs 하는 함수를 선언
def find(c, r, size):
    global graph
    global will_visit
    global count
    # current = []
    s = size
    graph[c][r] = '2'
    count += 1
    will_visit.append((c,r))
    list(set(will_visit))
    # while will_visit:
    print('will1', will_visit)
    current = will_visit.pop()
    print('will2', will_visit)
    print('current1',current)
    # print('will', will_visit)
    print('gr', graph)

    # if (current[0] - 1 > 0 and current[1] - 1 > 0 and current[0] + 1 != size and current[1] + 1 != size):
    print('current2 ', current)
    if graph[current[0]][current[1]-1] == '1' and current[1] - 1 > 0:
        print('11111111111111111111111')
        # graph[current[0]][current[1]-1] = '2'
        will_visit.append((current[0], current[1]-1))
        find(current[0], current[1]-1, s)

    elif graph[current[0]-1][current[1]] == '1' and current[0] - 1 > 0:
        print('22222222222222222222222222')
        # graph[current[0]-1][current[1]] = '2'
        will_visit.append((current[0]-1, current[1]))
        find(current[0]-1, current[1], s)

    elif graph[current[0]][current[1]+1] == '1' and current[1] + 1 < s:
        print('33333333333333333333333333')
        # graph[current[0]][current[1]+1] = '2'
        will_visit.append((current[0], current[1]+1))
        find(current[0], current[1]+1, s)

    elif graph[current[0]+1][current[1]] == '1' and current[0] + 1 < s:
        print('44444444444444444444444444')
        # graph[current[0]+1][current[1]] = '2'
        will_visit.append((current[0]+1, current[1]))
        find(current[0]+1, current[1], s)
    print('count " ', count)
    print('will_count', will_visit)
    # print(graph)
    # if not will_visit:
    #     ans.append(count)
        # count = 0
    # print('will_visit :::    ', will_visit)

    # if not (c - 1 < 0 or r - 1 < 0 or c + 1 == size or r + 1 == size):
    #     if graph[c][r-1] == '1':
    #         graph[c][r-1] = '2'
    #         will_visit.append((c, r-1))
    #         find(c, r-1, s)
    #     elif graph[c-1][r] == '1':
    #         graph[c-1][r] = '2'
    #         will_visit.append((c-1, r))
    #         find(c-1, r, s)
    #     elif graph[c][r+1] == '1':
    #         graph[c][r+1] = '2'
    #         will_visit.append((c, r+1))
    #         find(c, r+1, s)
    #     elif graph[c+1][r] == '1':
    #         graph[c+1][r] = '2'
    #         will_visit.append((c+1, r))
    #         find(c+1, r, s)
    # if not will_visit:
    #     print('count :: ', count)
    #     count = 0






count = 0
will_visit = []
ans = []

# 행,열의 크기(size) 와 전체 지도(graph)를 입력받음
graph = []
size = int(input())
for _ in range(size):
    ss = []
    for s in sys.stdin.readline().strip():
        ss.append(s)
        # print(ss)
    graph.append(ss)

print('graph', graph)

for col in range(size):
    for row in range(size):
        if graph[col][row] == '1':
            find(col, row, size)
            # print('count : ', count)
            # print('graph ', graph)
answer = sorted(ans)
print(len(ans))
for a in answer:
    print(a)