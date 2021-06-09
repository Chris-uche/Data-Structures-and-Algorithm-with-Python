import unittest
import searchinSorted


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(searchinSorted.searchInSorted(matrix, 1), [0, 0])
    def test_case_2(self):
        self.assertEqual(searchinSorted.searchInsorted(matrix, 2), [1, 0])
    def test_case_3(self):
        self.assertEqual(searchinSorted.searchSorted(matrix, 2), [1, 0])



















if __name__ == '__main__':
    unittest.main()