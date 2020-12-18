import sys

def solution(start, cnt):
    global sortedTime
    global answer
    ava = []
    start = start
    cnt = cnt
    idx = sortedTime.index(start)
    if idx + 1 == len(sortedTime):
        answer.append(cnt)
        return cnt

    sliced_sTime = sortedTime[idx+1:]

    for sst in sliced_sTime:
        if start[1] <= sst[0]:
            ava.append(sst)
        if not ava:
            pass
            # answer.append(cnt)
            # return cnt
        else:
            start = ava.pop(0)
            solution(start, cnt+1)


conference = int(sys.stdin.readline())
time = []
# time = deque()
answer = []
while conference > 0:
    a, b = sys.stdin.readline().split()
    a , b = int(a), int(b)
    time.append((a,b))

    conference -= 1
sortedTime = sorted(time)

# print(time)
# print(sortedTime)

for st in sortedTime:
    solution(st, 1)

print('answer list : ', answer)
print(max(answer))
# solution(sortedTime[0],0)
#  [(0, 6), (1, 4), (2, 13), (3, 5), (3, 8), (5, 7), (5, 9), (6, 10), (8, 11), (8, 12), (12, 14)]




