input = input()
m_input = input.split('-')
result = []
temp = 0

for m in m_input:
    for t in m.split('+'):
        temp += int(t)
    result.append(temp)
    temp = 0

for i in range(len(result)):
    if i == 0 :
        temp = result[i]
    else:
        temp = temp - result[i]
print(temp)