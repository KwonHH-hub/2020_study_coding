m, n = map(int, input().split())

print(m, n)

check = []
for _ in range(n):
    check = [[0]*m]
print(check)
graph = []
will_visit = []
for nn in range(n):
    graph.append(list(map(int, input().split(' '))))
print(graph)



# print(check)

def tomato(v, m, n):
    pdx = [0, 1]
    pdy = [1, 0]
    ndx = [0, -1]
    ndy = [-1, 0]
    print(will_visit)

    if v[0] + pdy[0] < m:
        pose = [v[0] + pdy[0], v[1]]
        will_visit.append(pose)

    if v[0] + ndy[0] > 0:
        pose = [v[0] + ndy[0], v[1]]
        will_visit.append(pose)
    if v[1] + pdx[1] < n:
        pose = [v[0], v[1] + pdx[1]]
        will_visit.append(pose)
    if v[1] + ndx[1] > 0:
        pose = [v[0], v[1] + ndx[1]]
        will_visit.append(pose)

    while will_visit:
        pose = will_visit.pop()
        tomato(pose, m, n)


v = [3,5]
tomato(v, m, n)