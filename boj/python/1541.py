# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 01:30:00 2021

"""

if __name__ == '__main__':
    nums_list = list(map(str, input().split('-')))
    num_list = []
    for i in nums_list:
        nums = i.split('+')
        num_sum = 0
        for num in nums:
            num_sum += int(num)
        num_list.append(num_sum)
    ans = num_list[0]
    for i in range(1, len(num_list)):
        ans -= num_list[i]
    print(ans)