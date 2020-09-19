# num = int(input())
# times = []
# for i in range(num):
#     times.append(list(map(int, (input().split(' ')))))
# st = 0
# ed = 0
# for s in range(len(times)):
#     if s == 0:
#         st = times[s][0]
#     else:
#         if st > times[s][0]:
#             st = times[s][0]
#
# for e in range(len(times)):
#     if e == 0:
#         ed = times[e][1]
#     else:
#         if ed < times[e][1]:
#             ed = times[e][1]
#
# print(st)
# print(ed)

# num = int(input())
# times = []
# time_min = 0
# time_max = 0
#
# for n in range(num):
#     times.append(list(map(int, input().split(' '))))
# for i in range(len(times)):
#     if i == 0:
#         time_min = times[i][0]
#         time_max = times[i][1]
#     else:
#         if times[i][0] < time_min:
#             time_min = times[i][0]
#         if times[i][1] > time_max:
#             time_max = times[i][1]
#
# print(time_min)
# print(time_max)
#


num = int(input())
min_delay = 0
last_time = 0
times = []
time_delay = []
count = 0
for n in range(num):
    times.append(list(map(int, input().split(' '))))

for t in times:
    if t == times[0]:
        last_time = t[1]
    else:
        if last_time < t[1]:
            last_time = t[1]
    time_delay.append(t[1]-t[0])
    if t == times[-1]:
        min_delay = min(time_delay)

print(min_delay)
print(last_time)
st_point = last_time
# print("min_delay", diff)
for tt in range(1, len(times)+1):
    diff = min_delay

    # print("st_point: ", st_point)
    if st_point - diff == times[-tt][0] :
        count = count + 1
        st_point = times[-tt][0]
    else:
        diff = diff + 1
        print("diff : ", diff)

print(count)