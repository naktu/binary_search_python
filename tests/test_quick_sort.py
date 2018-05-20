#!/usr/bin/env python
import unittest
import random
from quick_sort import quick_s_add_lists, quick_s_lomuto


class TestQuickSAndLists(unittest.TestCase):
    def setUp(self):
        n = 10
        self.to_sort = random.sample(list(range(n)), n)
        self.sorted = sorted(self.to_sort)

    def test_random(self):
        sor = quick_s_add_lists(self.to_sort)
        self.assertEqual(sor, self.sorted)

    def test_reversed(self):
        self.to_sort = list(reversed(sorted(self.to_sort)))
        sor = quick_s_add_lists(self.to_sort)
        self.assertEqual(sor, self.sorted)


class TestQuickSLomuto(unittest.TestCase):
    def setUp(self):
        n = 10
        self.to_sort = random.sample(list(range(n)), n)
        self.sorted = sorted(self.to_sort)

    def test_random(self):
        quick_s_lomuto(self.to_sort, 0, len(self.to_sort) - 1)
        self.assertEqual(self.to_sort, self.sorted)

    def test_reversed(self):
        self.to_sort = list(reversed(sorted(self.to_sort)))
        quick_s_lomuto(self.to_sort, 0, len(self.to_sort) - 1)
        self.assertEqual(self.to_sort, self.sorted)


if __name__ == '__main__':
    unittest.main()
