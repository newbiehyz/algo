# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:59:32 2021

@author: cn_hy
"""

def perm(s):
    result = []
    if len(s) <= 1:
        return s
    for i in range(len(s)):
        for j in perm(s[0:i]+s[i+1:]):
            result.append(s[i]+j)

    return result

res = perm(input())
res = set(res)
for i in sorted(res):
    print(i)