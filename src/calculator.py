from .custom_ex import IncorrectInputError
from functools import reduce
import operator
import math

class Calculator:
    def add(self,*args: float) -> float:
        return sum(args)
    
    def multiply(self, *args: float) -> float:
        result = 1
        try:
            for i in args:
                result *= i
            return result
        except TypeError:
            raise IncorrectInputError('Wrong Input')
        
    def subtract(self, *args: float) -> float:
        try:
            result = reduce(operator.__sub__, args)
            return result
        except TypeError:
            raise IncorrectInputError('Wrong Input')
    
    def divide(self, init, *args: float) -> float:
        result = init
        try:
            for i in args:
                result /= i
            return result
        except TypeError:
            raise IncorrectInputError('Wrong Input')
        
    def power(self, x: float, y: float) -> float:
        try:
            result = pow(x,y)
            return result
        except TypeError:
            raise IncorrectInputError('Wrong Input')
    
    def factorial(self, x: float) -> float:
        try:
            result = math.factorial(x)
            return result
        except TypeError:
            raise IncorrectInputError('Wrong Input')