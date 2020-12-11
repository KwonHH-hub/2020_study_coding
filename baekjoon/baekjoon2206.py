# import sys
# from collections import deque
# dx = [0,1,-1,0]
# dy = [1,0,0,-1]
#
# def find(n, m, visited):
#     global node
#     q = deque()
#
#     limit_x = len(node[0])
#     limit_y = len(node)
#     q.append((n,m))
#     count = 0
#     current_y = 0
#
#     while q:
#         current = q.popleft()
#         if current_y > current[0] :
#             continue
#         count += 1
#         current_x = current[1]
#         current_y = current[0]
#
#
#         if visited[current_y][current_x] == 0 and node[current_y][current_x] == '0':
#             visited[current_y][current_x] = 1
#
#         for d in range(len(dx)):
#             ambient_x = current_x + dx[d]
#             ambient_y = current_y + dy[d]
#
#             if ambient_x >= 0 and ambient_y >= 0 and ambient_x < limit_x and ambient_y < limit_y:
#                 if visited[ambient_y][ambient_x] == 0 and node[ambient_y][ambient_x] == '0':
#
#                     q.append((ambient_y, ambient_x))
#
#     if current_x == limit_x - 1 and current_y == limit_y - 1:
#         return count
#     else:
#         return -1
#
#
#
# n, m = map(int, input().split())
# node = []
# answer = []
# count = 0
#
# for _ in range(n):
#     temp = sys.stdin.readline().strip()
#     node.append(temp)
#
# for nn in range(n):
#     nd = node[nn]
#     for mm in range(m):
#         if nd[mm] == '1':
#             visited = [[0] * (m) for _ in range(n)]
#             node[nn] = nd[:mm] +'0'+ nd[mm+1:]
#             answer.append(find(0,0,visited))
#             node[nn] = nd[:mm] + '1' + nd[mm + 1:]
#
# answer = list(set(answer))
# answer.sort()
# answer.remove(-1)
#
# if answer:
#     print(answer[0])
# else:
#     print(-1)

































# ==========================================================================================================================



#
# import sys
# from collections import deque
# dx = [0,1,-1,0]
# dy = [1,0,0,-1]
#
# def find(n, m):
#     global node
#     global visited
#     q = deque()
#
#     limit_x = len(node[0])
#     limit_y = len(node)
#     q.append((n,m))
#     count = 0
#
#     wall_flag = False
#     wall_flag_pre = False
#
#     while q:
#         count += 1
#         current = q.popleft()
#         current_x = current[1]
#         current_y = current[0]
#
#         visited[current_y][current_x] = 1
#         print('visited: ',visited,'\n')
#
#         if wall_flag_pre == True and node[current_y][current_x] == '1':
#             print('Is wall flag setted??')
#             wall_flag = True
#         wall_flag_pre = False
#
#         prev_len = len(q)
#         for d in range(len(dx)):
#             ambient_x = current_x + dx[d]
#             ambient_y = current_y + dy[d]
#
#             if ambient_y >= 0 and ambient_y < limit_y and ambient_x >= 0 and ambient_x < limit_x:
#                 if wall_flag == False:
#                     if q and (ambient_y, ambient_x) == q[-1]:
#                         count -= 1
#                         wall_flag_pre = True
#                         q.popleft()
#                         if node[ambient_y][ambient_x] == '0' and visited[ambient_y][ambient_x] == 0 and (ambient_y, ambient_x) not in q:
#                             q.append((ambient_y, ambient_x))
#                     elif visited[ambient_y][ambient_x] == 0 and (ambient_y, ambient_x) not in q:
#                         q.append((ambient_y, ambient_x))
#
#                 else:
#                     if node[ambient_y][ambient_x] == '0' and visited[ambient_y][ambient_x] == 0 and (ambient_y, ambient_x) not in q:
#                         if (ambient_y, ambient_x) not in q:
#                             q.append((ambient_y, ambient_x))
#
#         if prev_len == len(q) and wall_flag == False:
#             print('q ::: ', q)
#             wall_flag = True
#             count -= 1
#             for d in range(len(dx)):
#                 ambient_x = current_x + dx[d]
#                 ambient_y = current_y + dy[d]
#
#                 if ambient_y >= 0 and ambient_y < limit_y and ambient_x >= 0 and ambient_x < limit_x:
#                     if visited[ambient_y][ambient_x] == 0 and (ambient_y, ambient_x) not in q:
#                         q.append((ambient_y, ambient_x))
#         print('current : ', current, '\nq :: ', q, '\ncount :: ', count, '\nwall flag = ', wall_flag)
#
#
#
#     if current_x == limit_x - 1 and current_y == limit_y - 1:
#         return count
#     else:
#         return -1
#
#
#
#
#
# n, m = map(int, input().split())
# node = []
# answer = []
# count = 0
#
# visited = [[0] * m for _ in range(n)]
#
# print('\n\nvisited : ',visited)
#
# for _ in range(n):
#     temp = sys.stdin.readline().strip()
#     node.append(temp)
#
# print('node : ',node, '\n')
#
# print('result = ',find(0,0))




# ======================= 다른 블로그의 답 참고하며 공부 ==========================================
# 출처 : https://sarc.io/index.php/algorithm/1937-baekjoon-online-judge-python-2206

from collections import deque

N,M=map(int,input().split(" "))
board=[list(map(int,input())) for _ in range(N)]
visit=[[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

move=[(1,0),(-1,0),(0,1),(0,-1)]

breakwall=False
q=deque()
q.append((0,0,1,breakwall))
visit[0][0][0] = 1
done = False
anslist=[]
while q:
    x,y,count,breakwallYN = q.popleft()
    if x == N-1 and y == M-1:
        anslist.append(count)
        done = True
        continue
    for i in range(4):
        xr = move[i][0]
        yr = move[i][1]
        if not (x + xr < N and x + xr >=0 and y + yr < M and y + yr >=0):
            continue
        else:
            if board[x + xr][y + yr] == 0:
                if breakwallYN and visit[1][x + xr][y + yr] == 0:
                    visit[1][x + xr][y + yr] = 1
                    q.append((x + xr, y + yr, count + 1, breakwallYN))
                elif not breakwallYN and visit[0][x + xr][y + yr] == 0:
                    visit[0][x + xr][y + yr] = 1
                    q.append((x + xr, y + yr, count + 1, breakwallYN))
            elif board[x + xr][y + yr] == 1 and not breakwallYN and visit[1][x + xr][y + yr] == 0:
                q.append((x + xr, y + yr, count + 1, True))
                visit[1][x + xr][y + yr] = 1

if done:
    print(min(anslist))
else:
    print(-1)
