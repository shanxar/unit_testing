import unittest
from ex2 import Calculator 


class TestCalculator_Addition(unittest.TestCase):
    
    def setUp(self) :
        
        self.obj_Calculator = Calculator()
        
        
    def test_addition(self):
        self.assertEqual(self.obj_Calculator.addition(80,19),99)
        self.assertEqual(self.obj_Calculator.addition(80,-19),61)
        self.assertEqual(self.obj_Calculator.addition(-80,-19),-99)
        
        


class TestCalculator_Division(unittest.TestCase):
    
    def setUp(self) :
        
        self.obj_Calculator = Calculator()
        
        
    def test_division(self):
        self.assertEqual(self.obj_Calculator.division(10,3),3)
        self.assertEqual(self.obj_Calculator.division(-10,2),-5)
        self.assertEqual(self.obj_Calculator.division(-80,-10),8)
        
        with self.assertRaises(Exception):
            self.obj_Calculator.division(10,0)
            

    
    

        