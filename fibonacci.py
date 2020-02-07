#!/Users/pratik/anaconda3/bin/python
# -*- coding: utf-8 -*-

__author__ = "Pratik Dubal"
__email__ = "psd2120 at columbia dot edu"


def fib_recursive(n):
    '''Computes the fibonacci number recursively.'''
    if n == 0 or n == 1:
        return n

    a = fib_recursive(n-1)
    b = fib_recursive(n-2)
    c = a + b

    return c


def fib_iterative(n):
    '''Computes the fibonacci number iteratively.'''
    a = 0
    b = 1

    for i in range(2, n+1):
        c = a + b
        a = b
        b = c

    return c


def fib_test():
    print('Fibonacci (Recursive) (n=5): ' + str(fib_recursive(5)))
    print('Fibonacci (Iterative) (n=5): ' + str(fib_iterative(5)))
    print('Fibonacci (Recursive) (n=20): ' + str(fib_recursive(20)))
    print('Fibonacci (Iterative) (n=20): ' + str(fib_iterative(20)))


if __name__ == "__main__":
    fib_test()
