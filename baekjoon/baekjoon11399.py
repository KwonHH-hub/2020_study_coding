people = int(input())
temp = 0
time = []

time = list(map(int, input().split(' ')))

time.sort()
for i in range(len(time)):
    temp += (len(time)-i)*time[i]

print(temp)