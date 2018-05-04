#!/usr/bin/env python
import unittest
from binary_search import list_generator

class TestListGenerators(unittest.TestCase):
    def test_list_1(self):
        result = list_generator(1)
        self.assertEqual(len(result[0]), 10)

    def test_list_couple(self):
        result = list_generator(3)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[2]), 1000)


if __name__ == '__main__':
    unittest.main()