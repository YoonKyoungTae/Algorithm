# coding=utf-8

## 버블정렬
## TODO : 앞의 원소와 뒤의 원소를 비교하여 큰 원소를 뒤로 보내 정렬한다.

def get_array():
    return [4213, 234, 324, 123, 12, 5, 345, 346, 34, 2354, 243, 34]

array = get_array()
size = len(array)

for x in range(size):
    for i in range(size - 1):
            before = array[i]
            after = array[i + 1]
            if before > after:
                array[i] = after
                array[i + 1] = before

print array
