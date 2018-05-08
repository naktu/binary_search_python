#!/usr/bin/env python
from typing import Tuple


def find_smallest(arr: list, step: int) -> Tuple[int, int]:
    """ Find smallest element in the list
    :param arr: list for sorting
    :param step: count of steps
    :return: index of smallest element and count of steps
    """
    smallest_i = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[smallest_i]:
            smallest_i = i
        step += 1
    return smallest_i, step


def selection_in_place(arr: list):
    """ Selection sort in place
    :param arr: list for sorting
    """
    step = 0
    for i in range(len(arr)):
        smallest_i = i
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                smallest_i = j
        step += 1
        arr[i], arr[smallest_i] = arr[smallest_i], arr[i]


def selection_sort(arr: list) -> Tuple[list, int]:
    """ Return sorted list and count steps
    :param arr:
    :return: sorted list and count of steps
    """
    new_array = []
    step = 0
    for i in range(len(arr)):
        smallest, step = find_smallest(arr, step)
        step += 1
        new_array.append(arr.pop(smallest))
    return new_array, step


def main():
    pass


if __name__ == '__main__':
    main()
