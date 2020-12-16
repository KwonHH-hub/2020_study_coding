# import sys
# import time
#
# def employ (tempB):
#     count = 1
#     for tb in range(1, len(tempB)):
#         ref = tempB[0:tb]
#         ref.sort()
#         if ref[0] > tempB[tb]:
#             count += 1
#     return count
#
#
#
# case = int(sys.stdin.readline())
#
#
# while case > 0:
#
#     tempA = []
#     tempB = []
#     A = []
#     B = []
#
#     time1 = time.time()
#
#     people = int(sys.stdin.readline())
#
#     for _ in range(people):
#         a, b = sys.stdin.readline().split(' ')
#         A.append(int(a))
#         B.append(int(b))
#
#     tempA = A[:]
#     tempA.sort()
#     tempB = []
#     for ta in range(len(tempA)):
#         i = A.index(tempA[ta])
#         tempB.append(B[i])
#
#     print(employ(tempB))
#     tempB = []
#     case -= 1
#
#     time2 = time.time()
#     print('time : ',case, '  ',time2-time1)


case = int(input())
print(case)
while case > 0:
    A = []
    B = []
    people = int(input())
    while people > 0:
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)
        people -= 1

    print(A)
    print(B)

    for

    case -= 1

