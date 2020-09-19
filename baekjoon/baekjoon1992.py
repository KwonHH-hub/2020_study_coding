image_size = int(input())
data = []
temp = 0
half = int(image_size / 2)
print(type(half))
result = []
for i in range(image_size):
    data.append(list(map(int, input())))
xp = 0
yp = 0
plane = 0
for _ in range(image_size):
    for s in range(half):
        for ss in range(half):
            temp += data[xp+s][yp+ss]
            print(temp)
        if s == half - 1 and ss == half - 1:
            plane += 1
            if plane == 1:
                xp = int(image_size/2)
            elif plane == 2:
                xp = 0
                yp = int(image_size / 2)
            elif plane == 3:
                plane = 0
                xp = int(image_size / 2)
                yp = int(image_size / 2)

            if temp == 0 or int(temp/(half*half)) == 1 :
                print("ss ", ss, "s ", s)
                result.append(int(temp/(half*half)))
                temp = 0
                if half == 1:
                    half = int(image_size / 2)
            else:
                half = int(half / 2)
print(result)