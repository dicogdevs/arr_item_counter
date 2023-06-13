import unittest
from arr_item_counter.arr_item_counter import arr_item_counter

class TestArrItemCounter(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(arr_item_counter([]), 0)

    def test_single_item(self):
        self.assertEqual(arr_item_counter([5]), 1)

    def test_multiple_items(self):
        self.assertEqual(arr_item_counter([1, 2, 3, 4, 5]), 5)