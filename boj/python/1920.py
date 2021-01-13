# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:20:44 2020

@author: EVer
"""

def BinarySearch(target, min, max, arr):
    while min <= max:
        mid = (min + max) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            min = mid + 1
        elif arr[mid] > target:
            max = mid - 1
    return 0

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    target = list(map(int, input().split()))
    arr = sorted(arr)
    for t in target:
        min = 0
        max = n - 1
        print(BinarySearch(t, min, max, arr))
        