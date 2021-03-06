# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 02:27:50 2021

"""

if __name__ == '__main__':
    n, target = map(int, input().split())
    num_max = 0
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] <= target:
                    num_max = max(num_max, nums[i] + nums[j] + nums[k])
    print(num_max)