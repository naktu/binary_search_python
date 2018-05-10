#!/usr/bin/env python
import unittest
from recursive_math import sum_r


class TestSumR(unittest.TestCase):
    def test_sum(self):
        arr = [0, 1, 2, 3, 4]
        self.assertEqual(10, sum_r(arr))


if __name__ == '__main__':
    unittest.main()
