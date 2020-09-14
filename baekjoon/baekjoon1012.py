# count = 0
# def dfs(graph, x, y):
#     global count
#     visit = []
#     for i in range(len(xy)):
#         x = xy[i][0]
#         y = xy[i][1]
#         graph[x][y] = 2
#         if graph[x+1][y] == 1:
#             visit.append([x+1, y])
#         if graph[x][y+1] == 1:
#             visit.append([x, y+1])
#         x = visit[0][0]
#         y = visit[0][1]
#         visit.remove([x,y])
#         dfs(graph, x, y)
#     # if graph[x][y] == 1:
#     #     if graph[x+1][y] == 1:
#     #         visit.append([x+1, y])
#     #     if graph[x][y+1] == 1:
#     #         visit.append([x, y+1])
#     #     else:
#     #         count = count + 1
#     # else:
#     #     x += 1
#     #     y += 1
#     # print('visit',visit)
#     # for _ in range(len(visit)):
#     #     x = visit[0][0]
#     #     print('x',x)
#     #     y = visit[0][1]
#     #     print('y',y)
#     #     visit.remove([x,y])
#     #     dfs(graph, x, y)
#
# test_case = int(input())
# graph = []
# xy = []
# for t in range(test_case):
#     m, n, k = map(int, input().split())
#     for mm in range(m):
#         temp = []
#         for nn in range(n):
#             temp.append(0)
#         graph.append(temp)
#     for i in range(k):
#         x, y = map(int, input().split())
#         xy.append([x, y])
#         graph[x][y] = 1
#     print(graph)
#     dfs(graph, 0, 0)
# print(count)
#
#
#
# '''
# 1000000000
# 1100000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# '''

def dfs(graph, x, y):
    visit = []
    for x, y in xy:
        graph[x][y] = 2
        if graph [x+1][y] == 1:
            visit.append([x+1, y])
        if graph [x][y+1] == 1:
            visit.append([x, y+1])
        dfs(graph, x, y)

test_case = int(input())
graph = []
xy = []
for t in range(test_case):
    m, n, k = map(int, input().split())
    for mm in range(m):
        temp = []
        for nn in range(n):
            temp.append(0)
        graph.append(temp)
    for i in range(k):
        x, y = map(int, input().split())
        xy.append([x, y])
        graph[x][y] = 1
    print(graph)
    dfs(graph, 0, 0)