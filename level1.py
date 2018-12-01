# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:53:16 2018

@author: Hesiris
"""


f = open('level1.txt')

s=0
for line in f:
    s=s+int(line)
    
print(s)