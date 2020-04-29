#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:49:09 2020

@author: Trinadh.Singaladevi
"""
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



