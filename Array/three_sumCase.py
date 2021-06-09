import unittest
import threenumberSum

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(threenumberSum.threenumberSum([1, 2, 3], 6), [[1, 2, 3]])
   
    def test_case_2(self):
        self.assertEqual(threenumberSum.threeNumSum([1, 2, 3], 6), [[1, 2, 3]])
   

if __name__ == '__main__':
    unittest.main()