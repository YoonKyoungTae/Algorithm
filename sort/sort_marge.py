# coding=utf-8

"""
[병합정렬]
리스트가 1개가 될 때 까지 원소를 분할 한 뒤, 병합하며 정렬하는 방식
"""


def get_array():
    return [10, 2, 5, 4, 7, 6, 8, 9, 3, 1]


# def divider(arr, start_idx, end_idx):
#     arr = arr[start_idx:end_idx]
#     print arr
#
#     if start_idx < end_idx and len(arr) != 1:
#         center = (0 + len(arr)) / 2
#         # print 'start_idx : %d, end_idx : %d' % (start_idx, end_idx)
#         # print 'center : %d, size : %d' % (center, len(arr))
#         divider(arr, 0, center)
#         divider(arr, center, len(arr))

def divider(arr, start_idx, end_idx):
    if start_idx < end_idx:
        center = (start_idx + end_idx) / 2

        divider(arr, start_idx, center)
        divider(arr, center + 1, end_idx)
        marge(arr, start_idx, center, end_idx)


def marge(arr, start_idx, center, end_idx):
    # print 'start : %d, center : %d, end : %d' % (start_idx, center, end_idx)

    if arr[start_idx] > arr[end_idx]:
        temp = arr[start_idx]
        arr[start_idx] = arr[end_idx]
        arr[end_idx] = temp

    print arr


array = get_array()

print array
divider(array, 0, len(array) - 1)
