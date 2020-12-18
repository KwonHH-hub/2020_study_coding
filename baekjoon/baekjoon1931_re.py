# import sys
#
# def solution(start, cnt):
#     global sortedTime
#     global answer
#     ava = []
#     start = start
#     cnt = cnt
#     idx = sortedTime.index(start)
#     if idx + 1 == len(sortedTime):
#         answer.append(cnt)
#         return cnt
#
#     sliced_sTime = sortedTime[idx+1:]
#
#     for sst in sliced_sTime:
#         if start[1] <= sst[0]:
#             ava.append(sst)
#         if not ava:
#             pass
#             # answer.append(cnt)
#             # return cnt
#         else:
#             start = ava.pop(0)
#             solution(start, cnt+1)
#
#
# conference = int(sys.stdin.readline())
# time = []
# # time = deque()
# answer = []
# while conference > 0:
#     a, b = sys.stdin.readline().split()
#     a , b = int(a), int(b)
#     time.append((b,a))
#
#     conference -= 1
# sortedTime = sorted(time, key=lambda time_ : time_[0])
#
# print(time)
# print(sortedTime)
#
# for st in sortedTime:
#     solution(st, 1)
#
# print('answer list : ', answer)
# print(max(answer))










import sys

def solution(time):
    cnt = 0
    ref = 0
    for st in time:
        if st[0] >= ref:
            cnt += 1
            ref = st[1]
    return cnt

conference = int(sys.stdin.readline())
time = []
while conference > 0:
    a, b = sys.stdin.readline().split()
    a , b = int(a), int(b)
    time.append((a,b))

    conference -= 1

time.sort(key = lambda time_ : (time_[1], time_[0]))

print(solution(time))
