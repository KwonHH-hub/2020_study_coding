def count(rank):
    cnt = 0
    for a in range(len(rank)):
        if a == 0:
            min = rank[a][1]
            cnt += 1
            continue
        if rank[a][1] < min:
            cnt += 1
            min = rank[a][1]
    return cnt





case = int(input())
while case > 0:
    rank = []

    people = int(input())
    while people > 0:
        a, b = map(int, input().split(' '))
        rank.append((a,b))
        people -= 1
    rank_ = sorted(rank)
    print(count(rank_))

    case -= 1