# 실패
# def dir(pose, dir):
#     if pose[0] == 6 or pose[1] == 4:
#         return
#     else:
#         return [pose[0]+dir[0], pose[1]+dir[1]]
#
#
# def find(start, check, graph):
#     graph[start[0]][start[1]] = 2
#     to_x = [dir(start,dx)[0],dir(start,dx)[1]]
#     to_y = [dir(start, dy)[0], dir(start, dy)[1]]
#     to_xy = [dir(start, dxdy)[0], dir(start, dxdy)[1]]
#     if graph[to_x[0]][to_x[1]] == 1:
#         check.append([to_x[0],to_x[1]])
#     if graph[to_y[0]][to_y[1]] == 1:
#         check.append([to_y[0],to_y[1]])
#     if graph[to_xy[0]][to_xy[1]] == 1:
#         check.append([to_xy[0],to_xy[1]])
#     start = c[0]
#     check.pop(0)
#     return start
#
#
# dx = [1, 0]
# dy = [0, 1]
# dxdy = [1, 1]
# c = []
# # graph = []
# start = [0,0]
# # n, m = map(int, input().split(' '))
# n, m = 4,6
# print(n,m)
# # graph = [list(map(int, input())) for _ in range(n)]
# graph = [
#         [1,0,1,1,1,1],
#         [1,0,1,0,1,0],
#         [1,0,1,0,1,1],
#         [1,1,1,0,1,1]
# ]
#
# print(graph)
# s = find(start,c,graph)
# k = find(s,c,graph)
# find(k,c,graph)
#
# # for _ in range(15):
# #     s = find(s,c,graph)
# print(graph)
graph = [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,1,1,1]]
n = 4
m = 6
linked = []
temp = []
for nn in range(n):
    for mm in range(m):
        if graph[nn][mm] == 1:
            if mm + 1 < m:
                pdx = [mm+1, nn]
                if graph[pdx[1]][pdx[0]] == 1:
                    temp.append(pdx)
            if mm - 1 > 0:
                ndx = [mm-1, nn]
                if graph[ndx[1]][ndx[0]] == 1:
                    temp.append(ndx)
            if nn + 1 < n:
                pdy = [mm, nn+1]
                if graph[pdy[1]][pdy[0]] == 1:
                    temp.append(pdy)
            if nn - 1 > 0:
                ndy = [mm, nn-1]
                if graph[ndy[1]][ndy[0]] == 1:
                    temp.append(ndy)
            linked.append(list(temp))
        else:
            linked.append(list(['e', 'e']))
# 0,0 방문하고, 연결된 노드가 방문한 노드에 없으면 check 에 넣고, 처음 좌표 빼고
print('linked')
print(linked,'\n')

visit = []
will_visit = [[0, 0]]

count = 0
while will_visit:
    current = will_visit.pop()
    visit.append(current)
    print('current',current)
    print('visit', visit)

    if ['e', 'e'] == linked[current[0]][current[1]]:
        print("hey")
        print(linked[current[1]])
        continue
    elif not (visit in linked[current[0]][current[1]]):
        will_visit.append(linked[current[0]][current[1]])

    print('will visit', will_visit)
    # break
    # print('current', current)
    # for l in linked[count]:
    #     print('l',l)
    #     if linked[check[0]][check[1]] in l:
    #         visit.append(list(linked[check[0]][check[1]]))
    #         print('append visit :',visit)
    count += 1
    # check.pop()
print(count)