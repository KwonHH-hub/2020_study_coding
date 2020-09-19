n, m, st = map(int, input().split(' '))
print(n,m,st)
node = [[]]
will_visit = []
visit = []
for mm in range(m):
    node.append(list(map(int, input().split(' '))))
    # print(temp)

print(node)
count = 0

def dfs (node, st):
    curr = st
    temp = []
    for x in node:
        if not x:
            continue
        if x[0] == curr:
            temp.append(x[1])
        will_visit.append(list(temp))
    while will_visit:
        curr = will_visit.pop()
        visit.append(curr)
        dfs(node,curr)

dfs(node, st)

print(visit)

