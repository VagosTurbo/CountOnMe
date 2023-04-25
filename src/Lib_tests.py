#!/usr/bin/env python3

import unittest
from mathlib import *

# To run this tests using this command: python -m unittest Lib_tests.py

expected_output = "ERROR" ########################### ERROR message

###################################################################################################

class TestAddition(unittest.TestCase): ########################### ADDITION tests 
    def test_addition_positive_Numbers(self):
        self.assertEqual(add(2, 3), '5')
        self.assertEqual(add(9, 7), '16')
        self.assertEqual(add(1000, 879), '1879')

    def test_addition_positive_negative_Numbers(self):
        self.assertEqual(add(-2, 3), '1')
        self.assertEqual(add(-2, 93), '91')
        self.assertEqual(add(92, -456), '-364')

    def test_addition_negative_Numbers(self):
        self.assertEqual(add(-2, -3), '-5')
        self.assertEqual(add(-80, -76), '-156')
        self.assertEqual(add(-70987, -357), '-71344')

###################################################################################################

class TestSubtraction(unittest.TestCase): ########################### SUBTRACTION tests 
    def test_subtraction_positive_Numbers(self):
        self.assertEqual(sub(1000, 500), '500')
        self.assertEqual(sub(457, 753), '-296')
        self.assertEqual(sub(34, 21), '13')

    def test_subtraction_positive_negative_Numbers(self):
        self.assertEqual(sub(900, -300), '1200')
        self.assertEqual(sub(-456, 379), '-835')
        self.assertEqual(sub(10000, -30000), '40000')

    def test_subtraction_negative_Numbers(self):
        self.assertEqual(sub(-123, -423), '300')
        self.assertEqual(sub(-678, -80), '-598')
        self.assertEqual(sub(900, -300), '1200')

###################################################################################################

class TestDivision(unittest.TestCase): ########################### DIVISION tests
    def test_division_positive_Numbers(self):
        self.assertEqual(div(50, 10), '5.0')
        self.assertEqual(div(753, 3), '251.0')
        self.assertEqual(div(2000, 2), '1000.0')
        self.assertEqual(div(50, 40), '1.25')

    def test_division_positive_negative_Numbers(self):
        self.assertEqual(div(570, -57), '-10.0')
        self.assertEqual(div(345, -10), '-34.5')
        self.assertEqual(div(6000, -200), '-30.0')

    def test_division_negative_Numbers(self):
        self.assertEqual(div(-300, -50), '6.0')
        self.assertEqual(div(-345, -100), '3.45')
        self.assertEqual(div(-18000, -300), '60.0')

    def test_zero_division(self): ########################### division by zero
        
        self.assertRaises(ZeroDivisionError, div, 678654, 0)
        self.assertRaises(ZeroDivisionError, div, -8700, 0)
        self.assertRaises(ZeroDivisionError, div, 0, 0)

###################################################################################################

class TestMultiplication(unittest.TestCase): ########################### MULTIPLICATION tests
    def test_multiplication_positive_Numbers(self):
        self.assertEqual(mul(570, 10), '5700')
        self.assertEqual(mul(789, 1), '789')
        self.assertEqual(mul(5, 5), '25')
        self.assertEqual(mul(200, 3), '600')
    
    def test_multiplication_positive_negative_Numbers(self):
        self.assertEqual(mul(89, -63), '-5607')
        self.assertEqual(mul(-7866, 1), '-7866')
        self.assertEqual(mul(-43, 10), '-430')

    def test_multiplication_negative_Numbers(self):
        self.assertEqual(mul(-3, -3), '9')
        self.assertEqual(mul(-4, -70), '280')
        self.assertEqual(mul(-70, -76), '5320')
    
    def test_zero_multiplication(self):
        self.assertEqual(mul(7890, 0), '0')
        self.assertEqual(mul(-990809, 0), '0')
        self.assertEqual(mul(0, 0), '0')

###################################################################################################
"""
class Testnthroot(unittest.TestCase): ########################### NTHROOT tests
    def test_nthroot_positive_Numbers(self):
        self.assertEqual(nthroot(9), 3)
        self.assertEqual(nthroot(169), 13)
        self.assertEqual(nthroot(400), 20)
        self.assertEqual(nthroot(7921), 89)

    def test_zero_nthroot(self):
        self.assertEqual(nthroot(0), 0)

    def test_nthroot_negative_Numbers(self): ########################### square root of negative numbers
        self.assertEqual(nthroot(-9), expected_output)
        self.assertEqual(nthroot(-121), expected_output)
        self.assertEqual(nthroot(-256), expected_output)
        self.assertEqual(nthroot(-9801), expected_output)
"""
###################################################################################################

class TestFactorial(unittest.TestCase): ########################### FACTORIAL tests
    def test_factorial_positive_Numbers(self):
        self.assertEqual(fact(9), '362880')
        self.assertEqual(fact(2), '2')
        self.assertEqual(fact(5), '120')
        self.assertEqual(fact(3), '6')
        self.assertEqual(fact(10), '3628800')

    def test_factorial_negative_Numbers(self): ########################### factorial of negative number doesn't exists
        self.assertRaises(ValueError, fact, -7)
        self.assertRaises(ValueError, fact, -3)
        self.assertRaises(ValueError, fact, -5)
        self.assertRaises(ValueError, fact, -1)

    def test_zero_factorial(self): ########################### factorial of zero is 1
        self.assertEqual(fact(0), '1')

###################################################################################################

class TestPwr(unittest.TestCase): ########################### RAISING TO A POWER tests
    def test_pwr_positive_Numbers(self):
        self.assertEqual(pwr(2,3), '8')
        self.assertEqual(pwr(8,2), '64')
        self.assertEqual(pwr(16,2), '256')
        self.assertEqual(pwr(9,3), '729')
        self.assertEqual(pwr(5,5), '3125')

    def test_pwr_positive_negative_Numbers(self):
        self.assertEqual(pwr(-4,2), '16')
        self.assertEqual(pwr(-5,3), '-125')
        self.assertEqual(pwr(2,-1), '0.5')
        self.assertEqual(pwr(5,-3), '0.008')
        self.assertEqual(pwr(-8,5), '-32768')

    def test_pwr_negative_Numbers(self):
        self.assertEqual(pwr(-5,-2), '0.04')
        self.assertEqual(pwr(-5,-1), '-0.2')
        self.assertEqual(pwr(-10,-1), '-0.1')

    def test_zero_pwr(self): ########################### any number raised to the power of 0 is 1
        self.assertEqual(pwr(10000, 0), '1')
        self.assertEqual(pwr(10757645000, 0), '1')
        self.assertEqual(pwr(4525356, 0), '1')
        self.assertEqual(pwr(654, 0), '1')
        self.assertEqual(pwr(8, 0), '1')

###################################################################################################

class TestNthRoot(unittest.TestCase): ########################### NTH ROOT tests
    def test_nthroot_positive_Numbers(self):
        self.assertEqual(nthroot(27, 3), '3.0')
        self.assertEqual(nthroot(125, 3), '5.0')
        self.assertEqual(nthroot(1296, 4), '6.0')
        self.assertEqual(nthroot(512, 9), '2.0')
        self.assertEqual(nthroot(117649, 6), '7.0')
        self.assertEqual(nthroot(0, 7), '0.0')

    def test_nthroot_positive_negative_Numbers(self):
        self.assertEqual(nthroot(1, -4), '1.0')
        self.assertEqual(nthroot(25, -2), '0.2')
        self.assertEqual(nthroot(400, -2), '0.05')

    def test_nthroot_negative_Numbers(self):
        self.assertEqual(nthroot(-125, -3), '-0.2')
        self.assertEqual(nthroot(-1024, -5), '-0.25')
        self.assertEqual(nthroot(-10000000, -7), '-0.1')

    def test_nthroot_positive_negative_even_Numbers(self): ########################### even number root of negative nember doesn't exixsts
        self.assertEqual(nthroot(-390625, 8), expected_output)
        self.assertEqual(nthroot(-4096, 4), expected_output)
        self.assertEqual(nthroot(-15625, 6), expected_output)
        self.assertEqual(nthroot(-6561, -8), expected_output)
        
        """self.assertRaises(ZeroDivisionError, nthroot, -390625, 8)
        self.assertRaises(ZeroDivisionError, nthroot, -4096, 4)
        self.assertRaises(ZeroDivisionError, nthroot, -15625, 6)
        self.assertRaises(ZeroDivisionError, nthroot, -6561, -8)
        """

    def test_nthroot_positive_negative_odd_Numbers(self): ########################### odd number root of negative number exists
        self.assertEqual(nthroot(-216, 3), '-6.0')
        self.assertEqual(nthroot(-16807, 5), '-7.0')
        self.assertEqual(nthroot(-8192, 13), '-2.0')

    def test_zero_nthroot(self): ########################### zeroth number root of any number doesn't exixsts
        self.assertRaises(ZeroDivisionError, nthroot, 234, 0)
        self.assertRaises(ZeroDivisionError, nthroot, 768547, 0)
        self.assertRaises(ZeroDivisionError, nthroot, -324234, 0)
    
    def test_nthroot_zero_Number(self): ########################### nth number root of zero is zero
        self.assertEqual(nthroot(0, 3), '0.0')
        self.assertRaises(ZeroDivisionError, nthroot, 0, -5)
        
###################################################################################################

class TestLN(unittest.TestCase): ########################### natural logarithm tests
    def test_ln_positive_numbers(self):
        self.assertEqual(ln(1), '0.0')
        self.assertEqual(ln(10), '2.302585092994046')
        self.assertEqual(ln(100), '2.0')
        self.assertEqual(ln(1000), '3')
        self.assertEqual(ln(78), '0')

    def test_ln_negative_numbers(self): ########################### natural logarithm of negative number doesn't existS
        self.assertRaises(ValueError, ln, -9)
        self.assertRaises(ValueError, ln, -8765)
        self.assertRaises(ValueError, ln, -532)
        self.assertRaises(ValueError, ln, -78)
        self.assertRaises(ValueError, ln, -632)
        self.assertRaises(ValueError, ln, -1)


    def test_ln_zero(self): ########################### natural logarithm of zero doesn't exist
        self.assertRaises(ValueError, ln, 0)

###################################################################################################
