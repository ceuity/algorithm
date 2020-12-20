# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 02:52:39 2020

@author: EVer
"""

def Permutation(arr, depth, n, k):
    if depth == k:
        print(arr)
        return
    for i in range(depth, n):
        arr[i], arr[depth] = arr[depth], arr[i]
        Permutation(arr, depth + 1, n, k)
        arr[i], arr[depth] = arr[depth], arr[i]
        
arr = [6, 10, 2]
answer = []
Permutation(arr, 0, len(arr), len(arr))
print(answer)