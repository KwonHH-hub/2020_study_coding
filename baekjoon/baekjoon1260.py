# 실패
# n, m, st = map(int, input().split(' '))
# print(n,m,st)
# node = [[]]
# will_visit = [1]
# visit = []
# for mm in range(m):
#     node.append(list(map(int, input().split(' '))))
#
# print('conut')
# print(node.count(1))
# start = 1
# print('node\n', node)
# curr = will_visit.pop()
# def dfs(node):
#     global curr
#
#     for nd in node:
#         # print('n', n)
#         if not nd:
#             continue
#         if nd[0] == curr:
#             # print('n0',n[0])
#             will_visit.append(nd)
#             # print('will visit', will_visit)
#         else:
#             break
#     visit.append(curr)
#     print('visit', visit)
#     curr = will_visit.pop(0)
#     print('최종', curr)
#     if len(visit) == n-1:
#         visit.append(curr)
#     while will_visit:
#         dfs(node)
#
# dfs(node)
# print(visit)


# 풀이 확인
# 출처 : https://pacific-ocean.tistory.com/260

def dfs(v):
    print(v, end=' ')
    visit[v] = 1

    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 0
    while (queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0


n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
print('\nvisit : ',visit)
print('\ns1 : ',s)
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
print('\ns2 : ',s)
dfs(v)
print()
bfs(v)