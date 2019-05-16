# coding=utf-8

"""
[계수(카운팅) 정렬]
크기를 기준으로 출력하는 알고리즘
원소의 조건이 작을수록 최고의 성능을 보이는 알고리즘

1. 배열의 최대값을 구한다.
2. 각 원소들의 개수를 구한다.
3. 원소들의 개수만큼 앞에서부터 출력한다.

"""


def get_array():
    return [10, 2, 5, 4, 7, 6, 8, 9, 3, 1]


def counting(arr, max_val):
    count = []
    result = []

    for i in range(max_val):
        count.insert(i, 0)

    for i in range(len(arr)):
        count[arr[i] - 1] += 1

    for i in range(max_val):
        if count[i] != 0:
            for z in range(count[i]):
                result.append(i + 1)

    return result


array = get_array()
size = len(array)

print '정렬 전 : ' + array.__str__()
max_val = max(array)
result_arr = counting(array, max_val)
print '정렬 후 : ' + result_arr.__str__()
