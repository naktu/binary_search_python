#!/usr/bin/env python
import unittest
import random
from binary_search import list_generator, binary_search_r, binary_search


class TestListGenerators(unittest.TestCase):
    def test_list_1(self):
        result = list_generator(1)
        for i in result:
            self.assertEqual(len(i), 10)

    def test_list_couple(self):
        count = 3
        result = list_generator(count)
        for i, j in enumerate(result, 1):
            self.assertEqual(len(j), 10**i)


class TestBinarySearchR(unittest.TestCase):
    def test_simple_list_0(self):
        for i in range(7, 17):
            test_list = list(range(2**i))
            numb_0 = 0
            index, steps = binary_search_r(
                numb_0, 0, len(test_list)-1, test_list)
            self.assertEqual(0, index)
            self.assertEqual(steps, i)

    def test_simple_list_last(self):
        for i in range(7, 17):
            test_list = list(range(2**i))
            numb_l = len(test_list)-1
            index, steps = binary_search_r(
                numb_l, 0, len(test_list)-1, test_list)
            self.assertEqual(numb_l, index)
            self.assertEqual(steps, i)

    def test_common_list_0(self):
        for i in range(7, 17):
            sample_list = list(range(2 ** (i+1)))
            common_list = sorted(random.sample(sample_list, 2 ** i))
            numb_0 = common_list[0]
            index, steps = binary_search_r(
                numb_0, 0, len(common_list)-1, common_list)
            self.assertEqual(0, index)
            self.assertEqual(steps, i)

    def test_common_list_last(self):
        for i in range(7, 17):
            sample_list = list(range(2 ** (i+1)))
            common_list = sorted(random.sample(sample_list, 2 ** i))
            numb_0 = common_list[-1]
            index, steps = binary_search_r(
                numb_0, 0, len(common_list)-1, common_list)
            self.assertEqual(len(common_list)-1, index)
            self.assertEqual(steps, i)


class TestBinarySearch(unittest.TestCase):
    def test_simple_list_0(self):
        for i in range(7, 17):
            test_list = list(range(2**i))
            numb_0 = 0
            index, steps = binary_search(
                numb_0, 0, len(test_list)-1, test_list)
            self.assertEqual(0, index)
            self.assertEqual(steps, i)

    def test_simple_list_last(self):
        for i in range(7, 17):
            test_list = list(range(2**i))
            numb_l = len(test_list)-1
            index, steps = binary_search(
                numb_l, 0, len(test_list)-1, test_list)
            self.assertEqual(numb_l, index)
            self.assertEqual(steps, i)

    def test_common_list_0(self):
        for i in range(7, 17):
            sample_list = list(range(2 ** (i+1)))
            common_list = sorted(random.sample(sample_list, 2 ** i))
            numb_0 = common_list[0]
            index, steps = binary_search(
                numb_0, 0, len(common_list)-1, common_list)
            self.assertEqual(0, index)
            self.assertEqual(steps, i)

    def test_common_list_last(self):
        for i in range(7, 17):
            sample_list = list(range(2 ** (i+1)))
            common_list = sorted(random.sample(sample_list, 2 ** i))
            numb_0 = common_list[-1]
            index, steps = binary_search(
                numb_0, 0, len(common_list)-1, common_list)
            self.assertEqual(len(common_list)-1, index)
            self.assertEqual(steps, i)


if __name__ == '__main__':
    unittest.main()
