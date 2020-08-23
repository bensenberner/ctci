"""
Naive solution: []
"""


def binary_search(arr, element):
    n = len(arr)
    low_idx, exclusive_end_idx = 0, n
    while low_idx < exclusive_end_idx:
        mid_idx = (low_idx + exclusive_end_idx) // 2
        if arr[mid_idx] == element:
            return mid_idx
        if arr[mid_idx] > element:
            exclusive_end_idx = mid_idx
        if arr[mid_idx] < element:
            low_idx = mid_idx + 1
    return -1


def find_element(matrix, element):
    for row_idx, row in enumerate(matrix):
        col_idx = binary_search(row, element)
        if col_idx != -1:
            return row_idx, col_idx
    return -1, -1
