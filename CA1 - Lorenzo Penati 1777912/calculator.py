# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:21:10 2017

@author: Lorenzo
"""
import math

#Add 2 numbers together
def add(first,second):
    fl_first = float(first)
    fl_second = float(second)
    return fl_first + fl_second

#Add 2 numbers together
def subtract(first,second):
    fl_first = float(first)
    fl_second = float(second)
    return fl_first - fl_second

#Multiply 2 numbers
def multiply(first,second):
    fl_first = float(first)
    fl_second = float(second)
    return round(fl_first * fl_second,5)

#Divide 2 numbers
def divide(first,second):
    fl_first = float(first)
    fl_second = float(second)
    if fl_second == 0:
        return 'undefined'
    return round(fl_first / fl_second,5)

#Square root
def squareRoot(first):
    fl_first = float(first)
    if fl_first < 0:
        return 'undefined'
    return round(math.sqrt(fl_first),3)

#Exponential
def exponential(first,second):
    fl_first = float(first)
    fl_second = float(second)
    return round(fl_first ** fl_second,5)

#Square
def square(first):
    fl_first = float(first)
    return round(fl_first * fl_first,5)

#Square
def cube(first):
    fl_first = float(first)
    return round(fl_first * fl_first * fl_first,5)

#Sine   
def sine(first):
    fl_first = float(first)
    return round(math.sin(fl_first), 2)

#Cosine   
def cosine(first):
    fl_first = float(first)
    return round(math.cos(fl_first), 2)


