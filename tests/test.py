import unittest

#Create our 'test case'
class MyTestCase(unittest.TestCase): #<name>TestCase
    def test_one(self): #A method of the test case should start with 'test'
        #Assertion
        self.assertTrue(True) #setting this to false produces F- Fail
        # result = add_two_numbers(4,5) #NameError
    def test_float_and_int(self):
        self.assertEqual(1, 1.0)
    
    def test_float_and_str(self):
        self.assertEqual(1,'1')

class MySecondTestCase(unittest.TestCase):
    def test_three(self):
        self.assertIsNone(None)

if __name__ == '__main__':
    unittest.main() #start our test runner