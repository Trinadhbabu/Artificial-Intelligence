#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:49:09 2020

@author: Trinadh.Singaladevi
"""
'''
Objective
In this challenge, we practice using multiple linear regression to predict housing prices. Check out the Resources tab for helpful videos!

Task
Charlie wants to buy a house. He does a detailed survey of the area where he wants to live, in which he quantifies, normalizes, and maps the desirable features of houses to values on a scale of  to  so the data can be assembled into a table. If Charlie noted  features, each row contains  space-separated values followed by the house price in dollars per square foot (making for a total of  columns). If Charlie makes observations about  houses, his observation table has  rows. This means that the table has a total of  entries.

Unfortunately, he was only able to get the price per square foot for certain houses and thus needs your help estimating the prices of the rest! Given the feature and pricing data for a set of houses, help Charlie estimate the price per square foot of the houses for which he has compiled feature data but no pricing.

Important Observation: The prices per square foot form an approximately linear function for the features quantified in Charlie's table. For the purposes of prediction, you need to figure out this linear function.

Recommended Technique: Use a regression-based technique. At this point, you are not expected to account for bias and variance trade-offs.

'''
import numpy as np
from sklearn.linear_model import LinearRegression
import sys

f,n = map(int,input().split())

train_data = []
test_data = []
[train_data.append(input().split()) for _ in range(n)]
t = int(input())
[test_data.append(input().split()) for _ in range(t)]

train_data = np.array(train_data, dtype = float)
test_data = np.array(test_data, dtype = float)

train_x = train_data[:,0:-1]
train_y = train_data[:,-1:]

lr = LinearRegression()

lr.fit(train_x,train_y)

pred = lr.predict(test_data)

# print numpy arrays without braces
np.savetxt(sys.stdout,pred,fmt = '%.2f')



