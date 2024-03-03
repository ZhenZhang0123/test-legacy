# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class test_triangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right Scalene','3,4,5 is a Right Scalene')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right Scalene','5,3,4 is a Right Scalene')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testNegativeInvalidInput(self): 
        self.assertEqual(classify_triangle(-1,1,2),'InvalidInput','-1,1,2 invalidInput: negative input')

    def testTooBigInvalidInput(self): 
        self.assertEqual(classify_triangle(201,201,300),'InvalidInput','201,201,300 InvalidInput: input too big')
    
    def testNotNumberInvalidInput(self): 
        self.assertEqual(classify_triangle('a',201,300),'InvalidInput','\'a\',201,300 InvalidInput: not a number')

    def testNotATriangle(self): 
        self.assertEqual(classify_triangle(1,1,2),'NotATriangle','1,1,2 not a triangle')

    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(2,3,4),'Scalene','2,3,4 should be Scalene')

    def testIsocelesTriangles(self): 
        self.assertEqual(classify_triangle(2,2,3),'Isoceles','2,2,3 should be isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

