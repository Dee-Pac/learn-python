import unittest
import sys

sys.path.append('/home/dmohanakumarchan/code/learn-python/testing')

from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):

    def test_inputType(self):
        f = Fibonacci()
        self.assertRaises(TypeError, f.calculate, "a")
        self.assertRaises(TypeError, f.calculate, 1.1)

    def test_calculation(self):
        f = Fibonacci()
        numAndRes = [(0,0),(10,55),(2,1),(1,1)]
        for n in numAndRes:
            self.assertAlmostEqual(f.calculate(n[0]), n[1])




    