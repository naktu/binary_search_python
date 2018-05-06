#!/usr/bin/env python
import random
from typing import List, Tuple


Lists = List[List[int]]


def binary_search_r(
        numb: int, l: int, r: int, a: list, step=0) -> Tuple[int, int]:
    """Recursive binary search algorithm
    :param numb: number for search
    :param l: left element
    :param r: right element
    :param a: list for search
    :param step: count of steps
    :return: element id, count steps
    """
    middle = round((l + r) / 2)
    guess = a[middle]
    step += 1
    if guess == numb:
        return middle, step
    elif guess > numb:
        return binary_search_r(numb, l, middle-1, a, step)
    else:
        return binary_search_r(numb, middle+1, r, a, step)


def list_generator(orders: int) -> List:
    """Generate list by count orders
    if orders 1 will return
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    if orders 3 wil return
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2,...,98, 99], [0, 1, 2,...,998,999]
    :param orders: count orders you need get
    :return: list lists count by order from 1 to n
    """
    sorted_lists = []
    for i in range(1, orders+1):
        sample_list = list(range(100 ** i))
        sorted_lists.append(sorted(random.sample(sample_list, 10**i)))
    print(sorted_lists)
    return sorted_lists


def main():
    pass

    # TODO interface for input size of lists TODO chose one list or more that one list
    # TODO this function like a demo


if __name__ == '__main__':
    main()
