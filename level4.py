# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:53:16 2018

@author: Hesiris
"""

import numpy as np

def hamming(a,b):
    n = min(len(a),len(b))
    dist = 0
    for i in range(n):
        if a[i]!=b[i]:
            dist += 1
    #dist+=abs(len(b)-len(a))
    return dist


f = open('level3.in')
lines = f.readlines()

#Dedikálva Gyurinak:
match = [(line,lines[j]) for i,line in enumerate(lines) for j in range(i,len(lines)) if hamming(line,lines[j])==1][0]
           
#olvshatóbb változat:
'''
match=[]
for i,line in enumerate(lines):
    for j in range(i,len(lines)):
        if hamming(line,lines[j])==1:
            match.append(line)
            match.append(lines[j])'''
            
result=''
for i,c in enumerate(match[0]):
    if c==match[1][i] :
        result += c

print(result)