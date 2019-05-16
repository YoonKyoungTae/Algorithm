# coding=utf-8

"""
[퀵 정렬]
1. 랜덤의 피벗(기준) 값을 하나 선택 후 피벗을 기준으로 작은 요소는 모두 왼쪽, 큰 요소는 모두 오른쪽으로 이동시킨다.
2. 피벗을 제외한 정렬된 좌측 우측을 다시 1번을 반복한다.
3. 쪼갠 리스트의 사이즈가 0이 될 때 까지 반복한다.
"""


def get_array():
    return [5, 2, 10, 4, 7, 6, 8, 9, 3, 1]


def change(arr, s, e):
    temp = arr[s]
    arr[s] = arr[e]
    arr[e] = temp


def sort(arr, pivot, end):
    if pivot >= end:
        return

    start = pivot + 1
    P = arr[pivot]

    print arr

    while start < end:
        while arr[start] < P:
            start += 1

        while arr[end] > P:
            end -= 1

        if start < end:
            change(arr, start, end)
        elif end < start:
            change(arr, pivot, start - 1)

    sort(arr, 0, start - 1)

    if start == 1:
        return

    sort(arr, start, len(arr) - 1)


array = get_array()
size = len(array)

print '정렬 전 : ' + array.__str__()
print sort(array, 0, size - 1)
print '정렬 후 : ' + array.__str__()
