# coding=utf-8

## 선택정렬
## TODO : 주어진 리스트 중에 최솟값을 찾는다.
## TODO : 그 값을 맨 앞에 위치한 값과 교체한다(패스(pass)).
## TODO : 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다

def get_array():
    return [10, 2, 5, 4, 7, 6, 8, 9, 3, 1]


array = get_array()
size = len(array)

for i in range(size):
    min_index = i

    for j in range(i + 1, size):
        if array[min_index] > array[j]:
            min_index = j

    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp

print array
