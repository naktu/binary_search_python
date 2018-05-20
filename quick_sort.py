#!/usr/bin/env python
import random


def quick_s_add_lists(arr: list) -> list:
    """
    Quick sort with new array
    :param arr: array to sort
    :return: new sorted array
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        less = []
        greater = []
        middle = []
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i < pivot:
                greater.append(i)
            else:
                middle.append(i)
        return quick_s_add_lists(less) + middle + quick_s_add_lists(greater)


def quick_s_lomuto(arr: list, low: int, high: int) -> None:
    """Quick sort by lomuto in place
    :param arr: array to sort
    :param low: first element in array part
    :param high: second element in last part
    :return: none
    """
    if not (high - low) < 1:
        pivot = high
        right = high - 1
        left = low
        while left <= right:
            while arr[left] < arr[pivot]:
                left += 1
            while arr[right] > arr[pivot]:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        else:
            arr[left], arr[pivot] = arr[pivot], arr[left]
        quick_s_lomuto(arr, low, left - 1)
        quick_s_lomuto(arr, left + 1, high)


def main():
    to_sort = [5, 3, 6, 2, 1, 0, 9, 8, 7, 4]
    print(to_sort)
    quick_s_lomuto(to_sort, 0, len(to_sort) - 1)
    print(to_sort)


if __name__ == '__main__':
    main()
