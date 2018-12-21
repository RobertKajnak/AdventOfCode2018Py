# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:53:16 2018

@author: Hesiris
"""

import numpy as np



f = open('level5.in')

x=[]
y=[]
w=[]
h=[]

for line in f:
    tokens = line.split(' ')
    a,b = tokens[2].split(',')
    x.append(int(a))
    y.append(int(b[:-1]))
    a,b = tokens[3].split('x')
    w.append(int(a))
    h.append(int(b[:-1]))
    
    
f.close()

#from functools import reduce
#maxW = reduce(max,x,y)

over = 0

A = np.zeros((2000,2000),np.byte)
for i in range (len(x)):
    for j in range(w[i]):
        for k in range(h[i]):
            idx = x[i]+k,y[i]+j
            if A[idx]==1:
                over+=1
                A[idx]=2
            elif A[idx]==0:
                A[idx]=1

#for i in A:
 #   for j in i:
  #      if j == 2:
   #         over+=1
print(over)