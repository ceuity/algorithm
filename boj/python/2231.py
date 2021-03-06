# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 02:35:20 2021

"""

if __name__=="__main__":
    n = int(input())
    length = len(str(n))
    if length > 2:
        n_min = n - length * 9
        n_max = n - length
    else:
        n_min = 0
        n_max = n
    def find_sum():
        for i in range(n_min, n_max + 1):
            if i + sum(map(int, str(i))) == n:
                print(i)
                return
        print(0)
    find_sum()