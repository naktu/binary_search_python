#!/usr/bin/env python
import random
from typing import List


Lists = List[List[int]]
steps = 0


def binary_search_r(numb: int, l: int, r: int, a: list) -> int:
    """
    Recursive binary search
    :param numb: number for search
    :param l: left element
    :param r: right element
    :param a: list for search
    :return: element number
    """


    global steps
    steps += 1
    return 1


def list_generator(orders: int) -> Lists:
    """
    :param orders: count orders you need get
    :return: list lists count by order from 1 to n
    if orders 1 will return
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    if orders 3 wil return
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2,...,98, 99], [0, 1, 2,...,998,999]
    """
    sorted_lists = []
    for i in range(1, orders+1):
        sample_list = list(range(100 ** i))
        sorted_lists.append(sorted(random.sample(sample_list, 10**i)))
    print(sorted_lists)
    return sorted_lists


def main():
    pass


if __name__ == '__main__':
    main()