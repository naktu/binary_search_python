#!/usr/bin/env python


def sum_r(arr: list) -> int:
    """sum elements in a list
    :param arr:
    :return: sum
    """
    if arr:
        return arr[0] + sum_r(arr[1:])
    return 0


def main():
    print("Start")
    count_elements = int(input("Enter count elements in a list: "))
    arr = list(range(count_elements))
    g = sum_r(arr)
    print("Sum of elements: {}".format(g))


if __name__ == '__main__':
    main()
