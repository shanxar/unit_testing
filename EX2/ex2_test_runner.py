import unittest
from ex2_test import  TestCalculator_Addition, TestCalculator_Division



def test_suite():
    test_suite_object= unittest.TestSuite()
    test_suite_object.addTest(unittest.makeSuite(TestCalculator_Addition))
    test_suite_object.addTest(unittest.makeSuite(TestCalculator_Division))
    print("TEST SUITE :", test_suite_object)
    return test_suite_object
    
if __name__=="__main__":
    file_obj= open("test_result.txt","w")
    runner= unittest.TextTestRunner(stream=file_obj,descriptions=True,verbosity=2)
    runner.run(test_suite())