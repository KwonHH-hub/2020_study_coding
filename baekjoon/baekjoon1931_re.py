import sys

def solution(start):
    cnt = 0
    global sortedTime
    global answer
    print('current start : ', start)
    idx = sortedTime.index(start)
    for tl in range(idx+1 , len(sortedTime)):
        if start == sortedTime[-1]:
            return cnt
        print('current timelist : ', sortedTime[tl])
        if sortedTime[tl][0] >= start[1]:
            print('selected : ', sortedTime[tl])
            print('')
            cnt += 1
            solution(sortedTime[tl])
    return cnt


conference = int(sys.stdin.readline())
time = []

while conference > 0:
    a, b = sys.stdin.readline().split()
    a , b = int(a), int(b)
    time.append((a,b))

    conference -= 1
sortedTime = sorted(time)

print(time)
print(sortedTime)

answer = []
for st in sortedTime:
    answer.append(solution(st))
    print('=========end==============')
    print(answer)


print('\n\n\n')
print('answer : ',answer)
# solution(sortedTime[0])
print(max(answer))

#  [(0, 6), (1, 4), (2, 13), (3, 5), (3, 8), (5, 7), (5, 9), (6, 10), (8, 11), (8, 12), (12, 14)]