import unittest
from ex1 import Calculator


class TestCalculator(unittest.TestCase):
    
    def setUp(self) :
        
        self.obj_Calculator = Calculator()
        
        
    def test_addition(self):
        self.assertEqual(self.obj_Calculator.addition(80,19),99)
        self.assertEqual(self.obj_Calculator.addition(80,-19),61)
        self.assertEqual(self.obj_Calculator.addition(-80,-19),-99)
        
        
    def test_division(self):
        self.assertEqual(self.obj_Calculator.division(10,3),3)
        self.assertEqual(self.obj_Calculator.division(-10,2),-5)
        self.assertEqual(self.obj_Calculator.division(-80,-10),8)
        
        with self.assertRaises(Exception):
            self.obj_Calculator.division(10,0)
            

    
    
if __name__=="__main__":
    unittest.main()
        