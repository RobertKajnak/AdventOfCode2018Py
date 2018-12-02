# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:53:16 2018

@author: Hesiris
"""

import numpy as np

f = open('level3.in')

alphabet = [chr(i) for i in range(ord('a'),ord('z'))]
twice = 0
thrice = 0

for line in f:
    charsums = np.zeros(ord('z')-ord('a')+1)
    for c in line:
        if c=='\n':
            break;
        charsums[(ord(c))-ord('a')] += 1;
    if sum([c1==2 for c1 in charsums])>0:
        twice += 1
        
    if sum([c1==3 for c1 in charsums])>0:
        thrice += 1
    
print(twice*thrice)