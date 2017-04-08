# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:21:10 2017

@author: Lorenzo
"""

from calculator import*
import unittest

# test for 2+2=4, 5+3=8, 0+4=4, 0+(-4)=-4
class MyTest(unittest.TestCase):
    def testAdd1(self):
        self.assertEqual(add(2,2),4)
    def testAdd2(self):
        self.assertEqual(add(5,3),8)
    def testAdd3(self):
        self.assertEqual(add(0,4),4)
    def testAdd4(self):
        self.assertEqual(add(0,-4),-4)
    def testAdd5(self):
        self.assertEqual(add(0.99999,0.00001),1)
        
# test for 2-2=0, 15-3=12, 4-0=4, 100-104=-4
    def testSubtract1(self):
        self.assertEqual(subtract(2,2),0)
    def testSubtract2(self):
        self.assertEqual(subtract(15,3),12)
    def testSubtract3(self):
        self.assertEqual(subtract(4,0),4)
    def testSubtract4(self):
        self.assertEqual(subtract(100,104),-4)
    def testSubtract5(self):
        self.assertEqual(subtract(1.00001,0.00001),1) 

# test for 2*2=4, 15*3=45, 4*0=0, some cases with many digits after the dot,
# and some negative numbers
    def testMultiply1(self):
        self.assertEqual(multiply(2,2),4)
    def testMultiply2(self):
        self.assertEqual(multiply(15,3),45)
    def testMultiply3(self):
        self.assertEqual(multiply(4,0),0)
    def testMultiply4(self):
        self.assertEqual(multiply(-4,-9),36)
    def testMultiply5(self):
        self.assertEqual(multiply(4.31345,-3.31345),-14.29240)
    def testMultiply6(self):
        self.assertEqual(multiply(14.33333,-2.99999),-42.99985) 

# test for 2/2=1, 15/3=5, 0/4=0
    def testDivide1(self):
        self.assertEqual(divide(2,2),1)
    def testDivide2(self):
        self.assertEqual(divide(15,3),5)
    def testDivide3(self):
        self.assertEqual(divide(0,4),0)
    def testDivide4(self):
        self.assertEqual(divide(4,0),'undefined')
    def testDivide5(self):
        self.assertEqual(divide(-10,4.0),-2.5)        
    def testDivide6(self):
        self.assertEqual(divide(-1000,5),-200)
               
# test for square root of 2, -4, 81, 2 and 10001
    def testSquareRoot1(self):
        self.assertEqual(squareRoot(4),2)
    def testSquareRoot2(self):
        self.assertEqual(squareRoot(-4),'undefined')
    def testSquareRoot3(self):
        self.assertEqual(squareRoot(81),9)
    def testSquareRoot4(self):
        self.assertEqual(squareRoot(2),1.414)        
    def testSquareRoot5(self):
        self.assertEqual(squareRoot(10001),100.005)        
        
# test for 2**2=4, 3**3=27, 4**0=1,2**5=32, 5**5=3125, 2**(-2)=0.25
#      and 10**(-5)=0.00001
    def testExponential1(self):
        self.assertEqual(exponential(2,2),4)
    def testExponential2(self):
        self.assertEqual(exponential(3,3),27)
    def testExponential3(self):
        self.assertEqual(exponential(4,0),1)
    def testExponential4(self):
        self.assertEqual(exponential(2,5),32)
    def testExponential5(self):
        self.assertEqual(exponential(5,5),3125)
    def testExponential6(self):
        self.assertEqual(exponential(2,-2),0.25)
    def testExponential7(self):
        self.assertEqual(exponential(10,-5),0.00001)       
        
# test for 2*2=4, (-2)*(-2)=4, 7*7=49, 0*0=0, 1*1=1 
#     and (-200.16)*(-200.16)=40064.0256
    def testSquare1(self):
        self.assertEqual(square(2),4)
    def testSquare2(self):
        self.assertEqual(square(-2),4)
    def testSquare3(self):
        self.assertEqual(square(-7),49)
    def testSquare4(self):
        self.assertEqual(square(0),0)
    def testSquare5(self):
        self.assertEqual(square(1),1)
    def testSquare6(self):
        self.assertEqual(square(-200.16),40064.0256)
        
# test for 2^3=8, (-2)^3=-8, (-7)^3=-243, 0^3=0,
#          1^3=1, (-1)^3)=-1 and -1.313^3 = -2.26357 
    def testCube1(self):
        self.assertEqual(cube(2),8)
    def testCube2(self):
        self.assertEqual(cube(-2),-8)
    def testCube3(self):
        self.assertEqual(cube(-7),-343)
    def testCube4(self):
        self.assertEqual(cube(0),0)
    def testCube5(self):
        self.assertEqual(cube(1),1)
    def testCube5(self):
        self.assertEqual(cube(-1),-1)
    def testCube6(self):
        self.assertEqual(cube(-1.313),-2.26357)        
        
# test for sin(0)=0, sin(pi/6)=0.5, sin(pi)=0, sin(3/2*pi)= -1, sin(pi/2)=1
    def testSine1(self):
        self.assertEqual(sine(0),0)
    def testSine2(self):
        self.assertEqual(sine(math.pi/6.0),0.5)  
    def testSine3(self):
        self.assertEqual(sine(math.pi),0)
    def testSine4(self):
        self.assertEqual(sine(3.0/2*math.pi),-1)
    def testSine5(self):
        self.assertEqual(sine(math.pi/2.0),1)
        
# test for cosin(0)= 1, cosin(pi/3)=0.5, cosin(pi)= -1,
#             cosin(3/2*pi)= 0, cosin(pi/2)= 0
    def testCosine1(self):
        self.assertEqual(cosine(0),1)
    def testCosine2(self):
        self.assertEqual(cosine(math.pi/3.0),0.5)        
    def testCosine3(self):
        self.assertEqual(cosine(math.pi),-1)        
    def testCosine4(self):
        self.assertEqual(cosine(3.0/2*math.pi),0)        
    def testCosine5(self):
        self.assertEqual(cosine(math.pi/2.0),0)        
        
                         
if __name__ == '__main__':
    unittest.main()
    
