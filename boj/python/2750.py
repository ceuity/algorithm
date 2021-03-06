# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 04:10:46 2021

"""

if __name__=='__main__':
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    nums.sort()
    for _ in nums:
        print(_)