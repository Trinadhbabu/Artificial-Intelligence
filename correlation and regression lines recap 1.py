#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:05:32 2020

@author: Trinadh.Singaladevi
"""

'''
problem statement:
    Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute Karl Pearson’s coefficient of correlation between these scores.
Compute the answer correct to three decimal places.

Output Format

In the text box, using the language of your choice, print the floating point/decimal value required. Do not leave any leading or trailing spaces.

For example, if your answer is 0.255. In python you can print using

print("0.255")

'''
x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]

def avge(a):
    return sum(a)/len(a)
    
def slope(x,y):
    x_dash = avge(x)
    y_dash = avge(y)
    numerator = sum([(yi-y_dash) * (xi-x_dash) for xi,yi in zip(x,y) ])
    denominator = sum([(xi-x_dash)**2 for xi in x]) * sum([(yi-y_dash)**2 for yi in y])
    return numerator/(denominator **0.5)



h = round(slope(x,y),3)
print(h)
