# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:13:38 2021

@author: cn_hy
"""

def fibo(n):
    if n == 3:
        return 2
    else:
        answer1 = 1
        answer2 = 1

        for i in range(n-2):
            answer = answer1 + answer2
            answer2 = answer1
            answer1 = answer
        return answer
        
n = int(input())
print(fibo(n))
