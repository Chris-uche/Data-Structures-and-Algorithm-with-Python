import unittest
import smallDiffereence

class TestProgram(unittest.TestCase):
    def test_case_2(self):
        self.assertEqual(
            smallDiffereence.smallestNumDifference(
                [10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031]
            ),
            [25, 1005],
        )
    
    def test_case_3(self):
        self.assertEqual(
            smallDiffereence.SmallestNumDiff(
                [10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031]
            ),
            [25, 1005],
        )
    

if __name__ == '__main__':
    unittest.main()