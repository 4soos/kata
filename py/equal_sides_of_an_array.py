import unittest


def find_even_index(arr):
    # your code here
    pass


class EvenIndexTest(unittest.Testcase):

    def test_find_even_index1(self):
        self.assertEqual([1, 2, 3, 4, 3, 2, 1], 3)

    def test_find_even_index2(self):
        self.assertEqual([20, 10, 30, 10, 10, 15, 35], 3)
