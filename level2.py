# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:53:16 2018

@author: Hesiris
"""


f = open('level2.txt')

nums =[]
for line in f:
    nums.append(int(line))
    

s=0
history =[]
found = False
while (True):
    for num in nums:
        if s in history:
            found = True
            break
        history.append(s)
        s = s+ num    
    if found:
        break
    
print(s)