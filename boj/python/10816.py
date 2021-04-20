# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:50:02 2020

@author: EVer
"""

# Timeout

def BinarySearch(target, min, max, arr):
    while min <= max:
        mid = (min + max) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            min = mid + 1
        elif arr[mid] > target:
            max = mid - 1
    return -1

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    target = list(map(int, input().split()))
    arr = sorted(arr)
    answer = []
    for t in target:
        min = 0
        max = n - 1
        index = BinarySearch(t, min, max, arr)
        count = 0
        i = 0
        j = 1
        if index >= 0:
            while True:
                if index + i < n and arr[index + i] == t:
                    count += 1
                    i += 1
                else:
                    break
            while True:
                if index - j >= 0 and arr[index - j] == t:
                    count += 1
                    j += 1
                else:
                    break
        answer.append(count)
    print(' '.join(map(str, answer)))