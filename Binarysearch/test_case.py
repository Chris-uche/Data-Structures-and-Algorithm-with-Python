import unittest
import binarysearch


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarysearch.binarySearch([1, 5, 23, 111], 111), 3)
   
    def test_case_2(self):
        self.assertEqual(binarysearch.binarySearchCase([1, 5, 23, 111], 5), 1)
   
    def test_case_3(self):
        self.assertEqual(binarysearch.binarySearchCaseThree([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
   
    def test_case_4(self):
        self.assertEqual(binarysearch.binarySearchCaseFour([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
   

    def test_case_5(self):
        self.assertEqual(binarysearch.binarySearchCaseFive([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
   
    def test_case_6(self):
        self.assertEqual(binarysearch.binarySearchCaseSix([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
   
    def test_case_7(self):
        self.assertEqual(binarysearch.binarySearchcaseSeven([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
   


if __name__ == '__main__':
    unittest.main()