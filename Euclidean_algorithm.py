#!/usr/bin/env python

def euclidean_r(a: int, b: int) -> int:
    """Recursive version of euclidean algorithm
    :param a: first number
    :param b: second number
    :return: grates common divisor
    """
    if a == b:
        return a
    elif a > b:
        d, m = divmod(a, b)
        if m == 0:
            return b
        else:
            return euclidean_r(m, b)
    else:
        d, m = divmod(b, a)
        if m == 0:
            return b
        else:
            return euclidean_r(a, m)


def euclidean(a: int, b: int) -> int:
    """Euclidean algorithm
    :param a: first number
    :param b: second number
    :return: grates common divisor
    """
    while True:
        if a == b:
            return a
        elif a > b:
             d, m = divmod(a, b)
             if m == 0:
                 return b
             else:
                 a = m
        else:
            d, m = divmod(b, a)
            if m == 0:
                return a
            else:
                b = m


def main():
    print("Start")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Recursive Euclidean algorithm:")
    gcd = euclidean_r(a, b)
    print("Grates common divisor : {}".format(gcd))
    print("-" * 79)
    print("Euclidean algorithm:")
    gcd = euclidean_r(a, b)
    print("Grates common divisor : {}".format(gcd))

if __name__ == '__main__':
    main()
