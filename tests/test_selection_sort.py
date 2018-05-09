#!/usr/bin/env python
import unittest
from selection_sort import find_smallest, selection_sort, selection_in_place


class TestFindSmallest(unittest.TestCase):
    def test_return_smallest(self):
        arr = [1, 2, 4, 5, 0, 6, 7]
        smallest, step = find_smallest(arr, 0)
        self.assertEqual(smallest, 4)
        self.assertEqual(step, len(arr)-1)

    def test_0(self):
        arr = []
        smallest, step = find_smallest(arr, 0)
        self.assertEqual(smallest, 0)


class TestSelectionSort(unittest.TestCase):
    def test_sort(self):
        arr = [1, 2, 4, 5, 0, 6, 7]
        new_array, step = selection_sort(arr)
        self.assertEqual(new_array, [0, 1, 2, 4, 5, 6, 7])


class TestSelectionSortInPlace(unittest.TestCase):
    def test_sort(self):
        arr = [1, 2, 4, 5, 0, 6, 7]
        step = selection_in_place(arr)
        self.assertEqual(arr, [0, 1, 2, 4, 5, 6, 7])
        self.assertEqual(step, 28)


if __name__ == '__main__':
    unittest.main()
