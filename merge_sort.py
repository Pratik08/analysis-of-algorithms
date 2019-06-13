#!/Users/pratik/anaconda3/bin/python
# -*- coding: utf-8 -*-

__author__ = "Pratik Dubal"
__email__ = "pratik dot dubal at columbia dot edu"

import math


def merge_inplace(arr, left, mid, right):
    ptr_left = left
    ptr_right = mid + 1
    res = []

    while(ptr_left <= mid and ptr_right <= right):
        if (arr[ptr_left] <= arr[ptr_right]):
            ptr_left += 1
        else:
            val = arr[ptr_right]
            idx = ptr_right
            while(idx != ptr_left):
                arr[idx] = arr[idx - 1]
                idx -= 1
            arr[ptr_left] = val
            ptr_left += 1
            mid += 1
            ptr_right += 1


def merge(arr, left, mid, right):
    arr_left = arr[left:mid + 1]
    arr_right = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while (i < len(arr_left) and j < len(arr_right)):
        if (arr_left[i] <= arr_right[j]):
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1

    while (i < len(arr_left)):
        arr[k] = arr_left[i]
        i += 1
        k += 1

    while (j < len(arr_right)):
        arr[k] = arr_right[j]
        j += 1
        k += 1


def merge_sort(arr, left, right, inplace=False):
    if (left == right):
        return
    mid = math.floor((left + right) / 2)
    merge_sort(arr, left, mid, inplace)
    merge_sort(arr, mid + 1, right, inplace)
    if (inplace):
        merge_inplace(arr, left, mid, right)
    else:
        merge(arr, left, mid, right)


def merge_sort_test():
    arr = [9, 6, 2, 5, 3, 2, 4, 8, 1, 7]
    merge_sort(arr, 0, 9)
    print('Sorted Array: ' + str(arr))


if __name__ == "__main__":
    merge_sort_test()
