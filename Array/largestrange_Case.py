import unittest
import largestRange

class TestProgram(unittest.TestCase):
   def test_case_1(self):
        self.assertEqual(largestRange.longestRange([4, 2, 1, 3]), [1, 4])

    

    

if __name__ == '__main__':
    unittest.main()