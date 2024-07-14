import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1,-1), -2)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        """Test the subraction method."""
        self.assertEqual(self.calc.subtract(5, 1), 4)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(1, 5), -4)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(1, 5), 5)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(1, 0), "None")