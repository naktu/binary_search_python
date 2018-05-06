#!/usr/bin/env python
import random
from typing import List, Tuple


Lists = List[List[int]]


def binary_search_r(
        numb: int, left: int, right: int, a: list, step=0) -> Tuple[int, int]:
    """Recursive binary search algorithm
    :param numb: number for search
    :param left: left element
    :param right: right element
    :param a: list for search
    :param step: count of steps
    :return: element id, count steps
    """
    middle = round((left + right) / 2)
    guess = a[middle]
    step += 1
    if guess == numb:
        return middle, step
    elif guess > numb:
        return binary_search_r(numb, left, middle - 1, a, step)
    else:
        return binary_search_r(numb, middle + 1, right, a, step)


def binary_search(
        numb: int, left: int, right: int, a: list) -> Tuple[int, int]:
    """Binary search algorithm
    :param numb:
    :param left:
    :param right:
    :param a:
    :return: element id, count steps
    """
    steps = 0
    while True:
        steps += 1
        middle = round((left + right) / 2)
        guess = a[middle]
        if guess == numb:
            return middle, steps
        elif guess > numb:
            right = middle - 1
        else:
            left = middle + 1


def list_generator(orders: int) -> List:
    """Generate list by count orders
    if orders 1 will return
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    if orders 3 will return
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2,...,98, 99], [0, 1, 2,...,998,999]
    :param orders: count orders you need get
    :return: list lists count by order from 1 to n
    """
    for i in range(1, orders+1):
        sample_list = list(range(100 ** i))
        yield sorted(random.sample(sample_list, 10**i))


def main():
    print("Start")
    count_orders = int(input("Enter the count orders: "))
    print("Recursive algorithm")
    list_check = list_generator(count_orders)
    for i in list_check:
        number = random.choice(i)
        print("Find number {}".format(number))
        index, steps = binary_search_r(number, 0, len(i) - 1, i)
        print("Index of number {0} is {1}".format(number, index))
        print("Steps {}".format(steps))
    print("-" * 10)
    print("While algorithm")
    list_check = list_generator(count_orders)
    for i in list_check:
        number = random.choice(i)
        print("Find number {}".format(number))
        index, steps = binary_search(number, 0, len(i) - 1, i)
        print("Index of number {0} is {1}".format(number, index))
        print("Steps {}".format(steps))


if __name__ == '__main__':
    main()
