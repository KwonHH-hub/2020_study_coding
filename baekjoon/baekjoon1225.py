import sys

A, B = sys.stdin.readline().split()
A_sum = 0
for a in A:
    A_sum += int(a)

B_sum = 0
for b in B:
    B_sum += int(b)

print(A_sum * B_sum)