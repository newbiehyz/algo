# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:05:43 2021

@author: cn_hy
"""

def fibo(n):
    if n > 2:
        return fibo(n-2) + fibo(n-1)
    else:
        return 1
    
n = int(input())
print(fibo(n))