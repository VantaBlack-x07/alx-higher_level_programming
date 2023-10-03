#!/usr/bin/python3
"""unittest max_intger"""

import unittest
max_intger = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests for max_int"""
    def test_normal_list(self):
        """sorted ;ist"""
        li = [1, 2, 3, 4, 5]
        x = max_intger(li)
        self.assertEqual(x, 5)

    def test_unsorted_list(self):
        """unsorted test"""
        li = [2,6,1,8,3,5]
        x = max_intger(li)
        self.assertEqual(x, 8)
        
    def test_double_max(self):
        """double test"""
        li = [2,6,1,8,8,5]
        x = max_intger(li)
        self.assertEqual(x, 8)
        
    def test_is_string(self):
        """unsorted test"""
        li = ["AAA", "BBB", "ZZZ"]
        x = max_intger(li)
        self.assertEqual(x, "ZZZ")

    def test_empty(self):
        """unsorted test"""
        li = []
        x = max_intger(li)
        self.assertEqual(x, None)

    def test_one_element(self):
        """unsorted test"""
        li = [2]
        x = max_intger(li)
        self.assertEqual(x, 2)

    def test_max_at_the_beg(self):
        """unsorted test"""
        li = [9, 3, 2, 1, 5]
        x = max_intger(li)
        self.assertEqual(x, 9)

if __name__ == '__main__':
    unittest.main()
