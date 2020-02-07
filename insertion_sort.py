#!/Users/pratik/anaconda3/bin/python
# -*- coding: utf-8 -*-

__author__ = "Pratik Dubal"
__email__ = "psd2120 at columbia dot edu"


def insertion_sort(arr):
    '''Performs insertion sort on arr'''
    if (len(arr) <= 1):
        return arr
    else:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while (j >= 0 and arr[j] >= key):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


def insertion_sort_test():
    print('Sorted Array: ' + str(insertion_sort([9, 6, 2, 5, 3, 2, 4, 8, 1])))
    print('Sorted Array: ' + str(insertion_sort([-9, -2, -5, -2, -4, -8, -1])))
    print('Sorted Array: ' + str(insertion_sort([9, -6, -2, -5, 2, -4, 8, 1])))


if __name__ == "__main__":
    insertion_sort_test()
