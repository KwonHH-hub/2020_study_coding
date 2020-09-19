n, m = map(int, input().split())
print("n", n)
print("m", m)
mmap = []
count = 0
flag = 0
r, c, d = map(int, input().split())
print("r", r)
print("c", c)
print("d", d)
# for nn in range(n):
#     for mm in range(m):
#         mmap.append(list(map(int, input().split())))
for nn in range(n):
    mmap.append(list(map(int, input().split())))
print("map : ", mmap)


#r 북쪽  n
#c 서쪽 m
print(d)
for t in range(n*m):
    if t == 0 and mmap[c][r] == 0:
        count = 1
    if d == 0:
        print("d=0")
        if flag == 3:
            r = r + 1
            continue

        if mmap[c-1][r] == 0:
            c = c - 1
            mmap[c][r] = 2
            count += 1
            flag = 0
        else:
            d = 3
            flag += 1
    if d == 1:
        print("d=1")
        if mmap[c][r-1] == 0:
            r = r - 1
            mmap[c][r] = 2
            count += 1
            flag = 0
        else:
            d = 0
    if d == 2:
        print("d=2")
        if mmap[c+1][r] == 0:
            c = c + 1
            mmap[c][r] = 2
            count += 1
            flag = 0
        else:
            d = 1
            flag += 1
    if d == 3:
        print("d=3")
        if mmap[c][r-1] == 0:
            r = r + 1
            mmap[c][r] = 2
            count += 1
            flag = 0
        else:
            d = 2
            flag += 1

print("count", count)


# if d == 0:
#     if mmap[c-1][r] == 0:
#         c = c - 1
#         mmap[c][r] = 2
#         # d = 3
#     else :
#         d = 3
# if d == 1:
#     if mmap[c][r+1] == 0:
#         r = r + 1
#         mmap[c][r] = 2
#         d = 2
#
# if d == 2:
#     if mmap[c+1][r] == 0:
#         c = c + 1
#         mmap[c][r] = 2
#         d = 1
#
# if d == 3:
#     if mmap[c][r-1] == 0:
#         r = r - 1
#         mmap[c][r] = 2
#         d = 0