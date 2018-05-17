#!/usr/bin/env python
import random



def quick_s_add_lists(arr: list) -> list:
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


def main():
    pass




if __name__ == '__main__':
    main()