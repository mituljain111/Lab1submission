# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#DIY1

import csv

f = open ('Lab01.csv')
count = 0
for row in csv.reader(f):
    if row != '\n':
        count += 1
print ('Number of rows:', count)


alist=[0]
for column in csv.reader(f):
    next(f)
    lab01[:10]=alist
    


    
#DIY2

import numpy as np

a=np.arange(5,16)
print(a)


b =np.linspace(0,23,7)
print(b)

c = np.random.uniform(low=-1, high=1, size=7)
print(c)

import matplotlib.pyplot as plt
d=np.sin(c)
plt.plot(c,d)

ra1 = np.random.randint(1,10,10)
ra2 = np.random.randint(11,20,10)
sub=ra2-ra1
dist=np.sqrt(sub)
print("Euclidean distance is ", dist)
