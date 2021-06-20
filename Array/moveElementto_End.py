import unittest
import moveElemToEnd

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = []
        toMove = 3
        expected = []
        output = moveElemToEnd.moveElemsToEnd(array, toMove)
        self.assertEqual(output, [])
    
    def test_case_2(self):
        array = []
        toMove = 3
        expected = []
        output = moveElemToEnd.MoveELementToTheEnd(array, toMove)
        self.assertEqual(output, [])


    
    

   
if __name__ == '__main__':
    unittest.main()