import sys
from collections import deque

def find(n, m):
    global count
    global node

    breakcount = 0
    breakFlag = -1
    breakChance = 0

    visited[n+1][m] = 1
    q = deque()
    q.append((n+1,m))

    while q:








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
