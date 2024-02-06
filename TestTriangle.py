# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import math
import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testNegativeInvalidInput(self): 
        self.assertEqual(classifyTriangle(-1,1,2),'InvalidInput','-1,1,2 invalidInput: negative input')

    def testTooBigInvalidInput(self): 
        self.assertEqual(classifyTriangle(201,201,300),'InvalidInput','201,201,300 InvalidInput: input too big')
    
    def testNotNumberInvalidInput(self): 
        self.assertEqual(classifyTriangle('a',201,300),'InvalidInput','\'a\',201,300 InvalidInput: not a number')

    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,1,2),'NotATriangle','1,1,2 not a triangle')

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be Scalene')

    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be isoceles')

    def testRightIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(2,2,2 * math.sqrt(2)),'Right Isoceles','2,2,2√2 should be right isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

