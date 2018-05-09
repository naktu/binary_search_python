#!/usr/bin/env python
import random
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
    :return step: count of steps
    """
    step = 0
    for i in range(len(arr)):
        smallest_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_i]:
                smallest_i = j
            step += 1
        step += 1
        arr[i], arr[smallest_i] = arr[smallest_i], arr[i]
    return step


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
    print("Start")
    count_elements = int(input("Enter the count of elements: "))
    print("Selection sort")
    list_check = random.sample(list(range(count_elements)), count_elements)
    print("Array:")
    print(list_check)
    new_arr, steps = selection_sort(list_check)
    print("Sorted array:")
    print(new_arr)
    print("Count of steps: {}".format(steps))
    print('-' * 79)

    print("Selection sort in place")
    list_check = random.sample(list(range(count_elements)), count_elements)
    print("Array:")
    print(list_check)
    steps = selection_in_place(list_check)
    print("Sorted array:")
    print(list_check)
    print("Count of steps: {}".format(steps))


if __name__ == '__main__':
    main()
