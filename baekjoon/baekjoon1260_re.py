import sys
from collections import deque

def draw_list(list, num):
    result = [[]]
    for n in range(1,num+1):
        str_num = str(n)
        temp = []
        for l in list:
            # temp = []
            if str_num in l:
                idx = (l.index(str_num) + 1) & 0x01
                temp.append(l[idx])
                temp.sort()
        result.append(temp)
    return result


def dfs(v, node):
    global dfs_result
    if not v in dfs_result:
        dfs_result.append(v)
    idx = int(v)
    while node[idx]:
        current = node[idx].pop(0)
        if not current in dfs_result:
            dfs(current, node)


def bfs(v, node):
    global bfs_result
    q = deque()
    q.append(v)
    while q:
        current = q.popleft()
        num_curr = int(current)
        if not current in bfs_result:
            bfs_result.append(current)

        while node[num_curr]:
            temp = node[num_curr].pop(0)
            if temp not in q and temp not in bfs_result:
                q.append(temp)



mnv = True
node = []
breakcount = 0

dfs_result = []
bfs_result = []


while True:

    if mnv:
        m,n,v = sys.stdin.readline().strip().split(' ')
        mnv = False
    else:
        breakcount += 1
        node.append(sys.stdin.readline().strip().split(' '))

    if breakcount == int(n):
        break

new_node = draw_list(node, int(m))
dfs(v, new_node)

new_node = draw_list(node, int(m))
bfs(v, new_node)


print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))