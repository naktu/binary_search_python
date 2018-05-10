#!/usr/bin/env python


def factorial(n: int) -> int:
    """ recursive factorial algorithm
    :param n: number for factorial
    :return: factorial of number
    """
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def non_recursive_factorial(n: int) -> int:
    """Non recursive factorial algorithm
    :param n: number for factorial
    :return: factorial of number
    """
    fac = 1
    while n:
        fac *= n
        n -= 1
    return fac


def main():
    print("Start")
    n = int(input("Enter number for factorial: "))
    print("Factorial algorithm")
    fac = factorial(n)
    print("{0}! = {1}".format(n, fac))
    print('-' * 79)

    print("Non recursive factorial algorithm")
    fac = non_recursive_factorial(n)
    print("{0}! = {1}".format(n, fac))


if __name__ == '__main__':
    main()
