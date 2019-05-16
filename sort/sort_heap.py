# coding=utf-8

"""
[힙정렬]
주어진 배열을 힙트리에 정리 한 후
정렬을 맥스힙(인덱스 0)과 마지막 인덱스의 위치를 교체한다.
"""


def get_array():
    return [10, 2, 5, 4, 7, 6, 8, 9, 3, 1]


def make_heap(arr, arr_size):
    for i in range(1, arr_size):
        child = i

        while child != 0:
            parent = (child - 1) / 2

            if arr[parent] < arr[child]:
                change(arr, parent, child)

            child = parent


def change(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


def sort(arr):
    count = len(arr) - 1

    while count != 0:
        change(arr, 0, count)
        make_heap(arr, count)
        count -= 1


array = get_array()
size = len(array)

print array
make_heap(array, size)
print array
sort(array)
print array
