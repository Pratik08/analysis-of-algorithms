#!/Users/pratik/anaconda3/bin/python
# -*- coding: utf-8 -*-

__author__ = "Pratik Dubal"
__email__ = "psd2120 at columbia dot edu"


def counting_sort(arr):
    '''Performs counting sort on arr'''
    n = len(arr)
    res = [float('Inf')] * n
    min_ele = float('Inf')
    max_ele = -float('Inf')

    for i in range(n):
        if arr[i] <= min_ele:
            min_ele = arr[i]
        if arr[i] >= max_ele:
            max_ele = arr[i]

    D = max_ele - min_ele
    count = [0] * (D + 2)

    if min_ele <= 0:
        adtv = abs(min_ele) + 1
    else:
        adtv = 0

    for i in range(n):
        count[arr[i] + adtv] += 1

    for i in range(2, D+2):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        res[count[arr[i] + adtv] - 1] = arr[i]
        count[arr[i] + adtv] -= 1

    return res


def counting_sort_test():
    print('Sorted Array: ' + str(counting_sort([9, 6, 2, 5, 3, 2, 4, 8, 1])))
    print('Sorted Array: ' + str(counting_sort([-9, -2, -5, -2, -4, -8, -1])))
    print('Sorted Array: ' + str(counting_sort([9, -6, -2, -5, 2, -4, 8, -1])))


if __name__ == "__main__":
    counting_sort_test()
