# coding=utf-8

## 삽입정렬
## TODO : k번째 원소를 1부터 k-1까지와 비교해 적절한 위치에 끼워넣고 그 뒤의 자료를 한 칸씩 뒤로 밀어내는 방식

def get_array():
    return [10, 2, 5, 4, 7, 6, 8, 9, 3, 1]
    # return [10, 2, 5]


array = get_array()
size = len(array)

# for i in range(size):
#     right = array[i]
#
#     print '=======', i, '번째 루프 ======='
#     for j in range(i, 0, -1):
#         left = array[j - 1]
#
#         print 'left : ', left
#         print 'right : ', right
#
#         if left > right:
#             array[j] = left
#             array[j - 1] = right
#         else:
#             print '통과'
#
#         print array

for i in range(size):
    right = array[i]
    index = 0
    # print '=======', i, '번째 루프 ======='
    for j in reversed(range(i)):
        # print '-<>-'
        print array

        left = array[j]

        # print ('%d > %d' % (left, right))

        if left > right:
            index = j
            array[j + 1] = left

        # print array

    array[index] = right

print array