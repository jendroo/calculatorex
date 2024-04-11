import unittest
from src.calculator import Calculator
from src.custom_ex import IncorrectInputError
from functools import reduce
import operator
import math

class CalculatorAddTestCase(unittest.TestCase): # Test Case
    def test_add_3_correct_input(self): # Unit
        #Arrage
        calculator = Calculator()
        x = 4
        y = 3
        z = 1
        expected_result = 8

        #Act
        result = calculator.add(x,y,z)

        #Assert
        self.assertEqual(result, expected_result)
    
    def test_add_with_no_args(self):
        #Arrange
        calculator = Calculator()
        expected_result = 0

        #ACt
        result = calculator.add()
        
        #Assert
        self.assertEqual(result, expected_result)

    def test_add_with_incorrect_input(self):
        # Arrange
        calculator = Calculator()
        x = '6'
        y = [4,5]

        # Act/Assert
        with self.assertRaises(TypeError):
            calculator.add(x,y)

class CalculatorMultiplyTestCase(unittest.TestCase):
    def setUp(self):
        print('SetUp Call')
        self.calculator = Calculator()

    def test_multiply_with_correct_input(self):
        
        x = 1
        y = 2
        z = 3
        expected_result = 6

        #Act
        result = self.calculator.multiply(x,y,z)

        #Assert
        self.assertEqual(result, expected_result)
    
    def test_multiply_with_incorrect_input(self):
        
        x = []
        y = (1,2)
        z = '4'

        with self.assertRaises(IncorrectInputError):
            self.calculator.multiply(x,y,z)

    def tearDown(self) -> None:
        print('tearDown Call')
        pass

class CalculatorSubTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
    
    def test_sub_with_correct_input(self):
        #Arrange
        x = 5
        y = 1
        z = 2

        expected_result = 2

        #Act
        result = self.calculator.subtract(x,y,z)

        #Assert
        self.assertEqual(result, expected_result)
    
    def test_sub_with_incorrect_input(self):
        x = []
        y = (1,2)
        z = '4'

        with self.assertRaises(IncorrectInputError):
            self.calculator.subtract(x,y,z)
    
class CalculatorDivTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_div_with_correct_input(self):
        x = 8
        y = 2
        z = 2

        expected_result = 2

        result = self.calculator.divide(x,y,z)

        self.assertEqual(result, expected_result)
    
    def test_div_with_incorrect_input(self):
        x = []
        y = (1,2)
        z = '4'

        with self.assertRaises(IncorrectInputError):
            self.calculator.divide(x,y,z)

class CalculatorPowTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_pow_with_correct_input(self):
        x = 2
        y = 4

        expected_result = 16

        result = self.calculator.power(x,y)

        self.assertEqual(result, expected_result)
    
    def test_pow_with_incorrect_input(self):
        x = []
        y = (1,2)

        with self.assertRaises(IncorrectInputError):
            self.calculator.power(x,y)

class CalculatorFactorialTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_fac_with_correct_input(self):
        x = 6

        expected_result = 720

        result = self.calculator.factorial(x)

        self.assertEqual(result, expected_result)
    
    def test_fac_with_incorrect_input(self):
        x = '5'

        with self.assertRaises(IncorrectInputError):
            self.calculator.factorial(x)
