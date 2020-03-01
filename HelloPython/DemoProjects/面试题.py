SIZE = 6
array = [[0] * SIZE]
for i in range(SIZE - 1):
    array += [[0] * SIZE]
# 得到二维列表
# print(array) 1~SIZE*SIZE
j, k = 0, 0
orient = 0
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i
    if orient == 0:
        j += 1
    elif orient == 1:
        k += 1
    elif orient == 2:
        k -= 1
    elif orient == 3:
        j -= 1

for elem in array:
    for e in elem:
        print('%02d' % e, end=' ')
    print('')
