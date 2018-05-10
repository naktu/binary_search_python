#!/usr/bin/env python
import unittest
from Euclidean_algorithm import euclidean, euclidean_r


class TestEuclideanRecursive(unittest.TestCase):
    def test_algorithm(self):
        gcd = euclidean_r(356896, 1545783)
        self.assertEqual(19, gcd)


class TestEuclidean(unittest.TestCase):
    def test_algorithm(self):
        gcd = euclidean(1545783, 356896)
        self.assertEqual(19, gcd)


if __name__ == '__main__':
    unittest.main()
