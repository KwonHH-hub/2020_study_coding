import sys

def count(rank):
    cnt = 1
    min = rank[0][1]
    for a in range(1, len(rank)):
        if rank[a][1] == 1:
            cnt += 1
            return cnt
        elif rank[a][1] < min:
            cnt += 1
            min = rank[a][1]
    return cnt

case = int(sys.stdin.readline())
while case > 0:
    rank = []

    people = int(sys.stdin.readline())
    while people > 0:
        a, b = sys.stdin.readline().split()
        a, b = int(a), int(b)
        rank.append((a,b))
        people -= 1
    rank_ = sorted(rank)
    print(count(rank_))

    case -= 1