import sys

# dfs 하는 함수를 선언
def find(c, r, g):
    print('c ',c)
    print('r ',r)
    print('\n')

    while not g:
        print()
        print('h')



visited = []
will_visit = []

# 행,열의 크기(size) 와 전체 지도(graph)를 입력받음
graph = []
size = int(input())
for _ in range(size):
    graph.append(sys.stdin.readline().strip())

print(graph)
print(size)

for col in range(size):
    print(col)
    for row in range(size):
        if graph[col][row] == 0:
            pass
        else:
            # print("here")
            if col + 1 == size or row + 1 == size:
                pass
            else:
                # print("here")
                if graph[col+1][row] == '1':
                    # print("here1")
                    will_visit.append((col+1, row))
                elif graph[col][row + 1] == '1':
                    # print('here2')
                    will_visit.append((col, row + 1))
                print(will_visit)
                current = will_visit[0]
                find(current[0], current[1],will_visit)

print(will_visit)