import sys
from collections import deque

def find(n, m):
    global count
    global node

    check = 0
    breakFlag = False
    ambient_ctrl = 0

    visited[n+1][m] = 1
    q = deque()
    q.append((n+1,m))

    while q:
        if not breakFlag:
            current = q.popleft()


        ambient_list = [(current[0],current[1]),
                        (current[0]+1,current[1]-1),
                        (current[0]+1,current[1]+1),
                        (current[0]+2,current[1])]

        if node[ambient_list[0][0]][ambient_list[0][1]] == '0' and visited[ambient_list[0][0]][ambient_list[0][1]] == 0 and ambient_list[0][0] > 0:
            print('h1')
            breakFlag = False
            check += 1

        if node[ambient_list[1][0]][ambient_list[1][1]] == '0' and visited[ambient_list[1][0]][ambient_list[1][1]] == 0 and ambient_list[1][1] > 0:
            print('h2')
            breakFlag = False
            check += 1

        if node[ambient_list[2][0]][ambient_list[2][1]] == '0' and visited[ambient_list[2][0]][ambient_list[2][1]] == 0 and ambient_list[2][1] < m:
            print('h3')
            breakFlag = False
            check += 1

        if node[ambient_list[3][0]][ambient_list[3][1]] == '0' and visited[ambient_list[3][0]][ambient_list[3][1]] == 0 and ambient_list[3][0] < n+1:
            print('h4')
            breakFlag = False
            check += 1

        if breakFlag == True:
            current = (ambient_list[ambient_ctrl][0]+ambient_list[-ambient_ctrl][0],ambient_list[ambient_ctrl][1]+ambient_list[-ambient_ctrl][1])
            print('cccc',current)

        if check == 0:
            print('here')
            q.appendleft(current)

            breakFlag = True
            current = ambient_list[ambient_ctrl]
            ambient_ctrl += 1

            if ambient_ctrl == 4:
                return -1







n, m = map(int, input().split())
print('\nn : ', n)
print('m : ', m)
visited = [[0] * (m) for _ in range(n+1)]
print('visited :\n',visited)
node = ['1'* m]
count = 0

for _ in range(n):
    temp = sys.stdin.readline().strip()
    node.append(temp)
print('node :\n',node)


find(0,0)
print('count :: ', count)

print('final visit value : \n',visited)
