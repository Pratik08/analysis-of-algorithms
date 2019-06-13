#!/Users/pratik/anaconda3/bin/python
# -*- coding: utf-8 -*-

__author__ = "Pratik Dubal"
__email__ = "pratik dot dubal at columbia dot edu"


from insertion_sort import insertion_sort
from merge_sort import merge_sort
import time
import random

for n in [10, 25, 50, 100, 500, 1000, 5000, 10000, 25000]:
    arr = [random.randint(1, 10000) for ele in range(n)]
    start_time = time.time()
    result = insertion_sort(arr)
    print('Insertion Sort (n = ' + str(n) + '): '
          + str(time.time() - start_time) + " seconds")
print("----------------------------------------------------------------------")
for n in [10, 25, 50, 100, 500, 1000, 5000, 10000, 25000, 500000]:
    arr = [random.randint(1, 10000) for ele in range(n)]
    start_time = time.time()
    merge_sort(arr, 0, n - 1, inplace=False)
    print('Merge Sort (n = ' + str(n) + '): '
          + str(time.time() - start_time) + " seconds")
print("----------------------------------------------------------------------")
for n in [10, 25, 50, 100, 500, 1000, 5000, 10000, 25000]:
    arr = [random.randint(1, 10000) for ele in range(n)]
    start_time = time.time()
    merge_sort(arr, 0, n - 1, inplace=True)
    print('Merge Sort (Inplace) (n = ' + str(n) + '): '
          + str(time.time() - start_time) + " seconds")
print("----------------------------------------------------------------------")
