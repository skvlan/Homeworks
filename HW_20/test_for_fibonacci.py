import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fib = Fibonacci()

    def test_zero(self):
        self.assertEqual(self.fib(0), 0, "Zero should have returned zero")

    def test_first(self):
        self.assertEqual(self.fib(1), 1, "One should return one")

    def test_second(self):
        self.assertEqual(self.fib(2), 1, "Two should return one")

    def test_sixth(self):
        self.assertEqual(self.fib(6), 8, "Six should return eight")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.fib(-1)
