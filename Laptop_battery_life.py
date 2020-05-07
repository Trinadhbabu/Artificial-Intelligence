# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
problem statement:
    Fred is a very predictable man. For instance, when he uses his laptop, all he does is watch TV shows. He keeps on watching TV shows until his battery dies. Also, he is a very meticulous man, i.e. he pays great attention to minute details. He has been keeping logs of every time he charged his laptop, which includes how long he charged his laptop for and after that how long was he able to watch the TV. Now, Fred wants to use this log to predict how long will he be able to watch TV for when he starts so that he can plan his activities after watching his TV shows accordingly.

Challenge

You are given access to Fred’s laptop charging log by reading from the file “trainingdata.txt”. The training data file will consist of 100 lines, each with 2 comma-separated numbers.

The first number denotes the amount of time the laptop was charged.
The second number denotes the amount of time the battery lasted.
The training data file can be downloaded here (this will be the same training data used when your program is run). The input for each of the test cases will consist of exactly 1 number rounded to 2 decimal places. For each input, output 1 number: the amount of time you predict his battery will last.

Sample Input

1.50

Sample Output

3.00

'''
'''
Approach:
    if you obsever traning data carefully and plot a line graph, you can find a pattern followed. if the number is less than or equal to 4 then output is double the number, otherwise the output is 8
'''

'''
import seaborn as sns
print(df[df[1]>=8])
sns.lineplot(x=x,y = y)
'''
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    p = float(input())
    if p <=4:
        print(p*2)
    else:
        print(8.0)