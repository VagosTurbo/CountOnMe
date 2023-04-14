import unittest
from mathlib import add
from mathlib import sub
from mathlib import div
from mathlib import mul


class TestAddition(unittest.TestCase):
    def test_addition_positive_Numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(9, 7), 16)
        self.assertEqual(add(1000, 879), 1879)

    def test_addition_positive_negative_Numbers(self):
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-2, 93), 91)
        self.assertEqual(add(92, -456), -364)

    def test_addition_negative_Numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-80, -76), -156)
        self.assertEqual(add(-70987, -357), -71344)

class TestSubtraction(unittest.TestCase):
    def test_substraction_positive_Numbers(self):
        self.assertEqual(sub(1000, 500), 500)
        self.assertEqual(sub(457, 753), -296)
        self.assertEqual(sub(34, 21), 13)

    def test_substraction_positive_negative_Numbers(self):
        self.assertEqual(sub(900, -300), 1200)
        self.assertEqual(sub(-456, 379), -835)
        self.assertEqual(sub(10000, -30000), 40000)

    def test_substraction_negative_Numbers(self):
        self.assertEqual(sub(-123, -423), 300)
        self.assertEqual(sub(-678, -80), -598)
        self.assertEqual(sub(900, -300), 1200)

class TestDivision(unittest.TestCase):
    def test_division_positive_Numbers(self):
        self.assertEqual(div(50, 10), 5)
        self.assertEqual(div(753, 3), 251)
        self.assertEqual(div(2000, 2), 1000)
        self.assertEqual(div(50, 40), 1.25)

    def test_division_positive_negative_Numbers(self):
        self.assertEqual(div(570, -57), -10)
        self.assertEqual(div(345, -10), -34.5)
        self.assertEqual(div(6000, -200), -30)

    def test_division_negative_Numbers(self):
        self.assertEqual(div(-300, -50), 6)
        self.assertEqual(div(-345, -100), 3.45)
        self.assertEqual(div(-18000, -300), 60)
"""
    def test_zero_division(self):
        expected_output = "Math, error!"
        expected_output_2 = "Undefined result!"
        self.assertEqual(div(-8700, 0), expected_output)
        self.assertEqual(div(678654, 0), expected_output)
        self.assertEqual(div(0, 0), expected_output_2)
"""
class TestMultiplication(unittest.TestCase):
    def test_multiplication_positive_Numbers(self):
        self.assertEqual(mul(570, 10), 5700)
        self.assertEqual(mul(789, 1), 789)
        self.assertEqual(mul(5, 5), 25)
        self.assertEqual(mul(200, 3), 600)
    
    def test_multiplication_positive_negative_Numbers(self):
        self.assertEqual(mul(89, -63), -5607)
        self.assertEqual(mul(-7866, 1), -7866)
        self.assertEqual(mul(-43, 10), -430)

    def test_multiplication_negative_Numbers(self):
        self.assertEqual(mul(-3, -3), 9)
        self.assertEqual(mul(-4, -70), 280)
        self.assertEqual(mul(-70, -76), 5320)
    
    def test_zero_multiplication(self):
        self.assertEqual(mul(7890, 0), 0)
        self.assertEqual(mul(-990809, 0), 0)
        self.assertEqual(mul(0, 0), 0)





















