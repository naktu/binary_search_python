#!/usr/bin/env python
import unittest
from factorial import factorial, non_recursive_factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(10), 3628800)


class TestNonRecursiveFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(non_recursive_factorial(10), 3628800)


if __name__ == '__main__':
    unittest.main()
