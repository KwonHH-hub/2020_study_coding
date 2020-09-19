# 실패

start = [0,0]

# size = int(input())
# gra = map(int, input().split())

size = 7
gra = [[0,1,1,0,1,0,0],[0,1,1,0,1,0,1],[1,1,1,0,1,0,1],[0,0,0,0,1,1,1],[0,1,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,0,0,0]]


visit = []
will_visit = [[0,0]]


count = 0
curr = will_visit.pop()

def find (gra, start = [0,0]):
    while True:
        print('will',will_visit)
        curr = will_visit.pop()
        if gra[curr[0]][curr[1] + 1] == 1:
            will_visit.append([curr[0], curr[1] + 1])
            gra[curr[0]][curr[1] + 1] = 2
            find(gra, [curr[0]][curr[1] + 1])

            # visit.append(curr)
        elif gra[curr[0] + 1][curr[1]] == 1:
            will_visit.aeepnd([curr[0], curr[1] + 1])
            gra[curr[0] + 1][curr[1]] = 2
            find(gra, [curr[0] + 1][curr[1]])

        else:
            break




print(curr)
while 1:
    find(gra)
    count += 1
    # break

print(will_visit)
print(count)
