#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:57:17 2020

@author: Trinadh.Singaladevi
"""
'''
problem statement:
    Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
When a student scores 10 in Physics, what is his probable score in History? Compute the answer correct to one decimal place.

Output Format

In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces. Your answer may look like: 5.5

This is NOT the actual answer - just the format in which you should provide your answer.

'''
x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]

def avge(a):
    return sum(a)/len(a)
    
def slope(x,y):
    x_dash = avge(x)
    y_dash = avge(y)
    numerator = sum([(yi-y_dash) * (xi-x_dash) for xi,yi in zip(x,y) ])
    denominator = sum([(xi-x_dash)**2 for xi in x])
    return numerator/denominator

def interceptor(x,y):
    b = slope(x,y)
    return avge(y) - (b * avge(x))

p = 10
h = slope(x,y)*p + interceptor(x,y)
print(h)



