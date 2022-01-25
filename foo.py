# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:19:58 2022

@author: jtrelles
"""

def is_divisible_by_k(x, k):
 '''
 Checks whether x is divisible by k.
 '''
 if x%k == 0:
       return True
 else:
       return False
 

'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000 (excluding doubles)
'''
x = []
for i in range(1000):
     
        if  (is_divisible_by_k(i, 2) | is_divisible_by_k(i, 5) | is_divisible_by_k(i, 7)):
            x.append(i)
        else:
            continue
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000 (excluding doubles)
'''
print(sum(x))


