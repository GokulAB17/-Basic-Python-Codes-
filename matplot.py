# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:02:01 2020

@author: Karan
"""


import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(1,11) 
y = 2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption")  m
plt.plot(x,y,"ob") 
plt.show()