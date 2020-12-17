import sys

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