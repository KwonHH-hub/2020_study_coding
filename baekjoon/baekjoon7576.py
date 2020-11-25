m, n = map(int, input().split())
print(m, n)

gra = []
for _ in range(n):
    gra.append(list(map(int, input().split(' '))))
print(gra)

check = [[0 for _ in range(m)] for _ in range(n)]
print(check)

# print(check)
will_visit = []
count = 0

def tomato(v):
    global count
    count += 1
    pdx = [0, 1]
    pdy = [1, 0]
    ndx = [0, -1]
    ndy = [-1, 0]

    check[v[0]][v[1]] = 2


    pose = [v[0], v[1] + pdx[1]]
    if v[1] + pdx[1] < m and check[pose[0]][pose[1]] != 2:
        # check[pose[0]][pose[1]] = 2
        will_visit.append([pose[0],pose[1]])

        print('1wv',will_visit)
        # tomato(will_visit.pop(-1))
        print('1p',pose)
        print('1c', check)

    pose = [v[0] + pdy[1], v[1]]
    if v[0] + pdy[1] < n and check[pose[0]][pose[1]] != 2:
        # check[pose[0]][pose[1]] = 2
        will_visit.append([pose[0], pose[1]])

        print('2wv', will_visit)
        # tomato(will_visit.pop(-1))
        print('2p', pose)
        print('2c', check)

    pose = [v[0], v[1] + ndx[1]]
    if v[1] + ndx[1] > 0 and check[pose[0]][pose[1]] != 2:
        # check[pose[0]][pose[1]] = 2
        will_visit.append([pose[0], pose[1]])

        print('3wv', will_visit)
        # tomato(will_visit.pop(-1))
        print('3p', pose)
        print('3c', check)

    pose = [v[0] + ndy[1], v[1]]
    if v[0] + ndy[1] > 0 and check[pose[0]][pose[1]] != 2:
        # check[pose[0]][pose[1]] = 2
        will_visit.append([pose[0], pose[1]])

        print('4wv', will_visit)
        # tomato(will_visit.pop(-1))
        print('4p', pose)
        print('4c', check)

    while will_visit:
        v = will_visit.pop(-1)
        tomato(v)


v = [3,5]
tomato(v)
print('check2',check)
print(count)