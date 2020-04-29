#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:34:10 2020

@author: Trinadh.Singaladevi
"""

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

print(round(slope(x,y)),3)