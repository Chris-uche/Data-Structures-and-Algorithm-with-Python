import unittest
import twoSum

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(twoSum.twoNumberSum([-4,-1,1,3,5,6,8,11], 13),[5,8])
    def test_case_2(self):
        self.assertEqual(twoSum.twoNumSum([-4,-1,1,3,5,6,8,11], 13),[5,8])

    

if __name__ == '__main__':
    unittest.main()