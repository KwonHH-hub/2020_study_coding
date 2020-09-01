# 틀린 코드
# weight = int(input())
# count = 1
# temp = 0
# while count:
#     temp = weight
#     count = temp // 5
#     temp -= 5 * count
#     if temp < 5:
#         break
# if temp % 3 == 0:
#     count += 1
#     print(count)
# else:
#     if weight % 3 == 0:
#         while count:
#             count = weight // 3
#             weight -= count * 3
#             if weight < 3:
#                 print(count)
#                 break
#     else:
#         print(-1)

# 틀린코드
# weight = int(input())
# if weight % 5 == 0:
#     print(weight // 5)
# else :
#     if (weight % 5) % 3 == 0:
#         print(weight//5 + (weight - weight//5 * 5) // 3)
#     elif weight % 3 == 0:
#         print(weight // 3)
#     else :
#         print(-1)

