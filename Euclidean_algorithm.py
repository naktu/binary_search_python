#!/usr/bin/env python

def euclidean_r(a: int, b: int) -> int:
    """Recursive version of euclidean algorithm
    :param a: first number
    :param b: second number
    :return: grates common devisor
    """
    if a == b:
        return a
    elif a > b:
        return euclidean_r(b, a-b)
    else:
        return euclidean_r(a, b-a)

def euclidean(a: int, b: int) -> int:
    """Euclidean algorithm
    :param a: first number
    :param b: second number
    :return: grates common devisor
    """
    while True:
        if a == b:
            return a
        elif a > b:
            a -= b
        else:
            b -= a


def main():
    f = euclidean(356896, 1545783)
    print(f)


if __name__ == '__main__':
    main()
