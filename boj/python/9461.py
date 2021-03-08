# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:33:56 2021

"""

if __name__=="__main__":
    n = int(input())
    
    def pado(n):
        if n not in dict:
            dict[n] = pado(n-5) + pado(n-1)
        return dict[n]
    
    for _ in range(n):
        dict = {}
        dict[0] = 0
        dict[1] = 1
        dict[2] = 1
        dict[3] = 1
        dict[4] = 2
        p = int(input())
        print(pado(p))

"""
규칙을 찾아서 점화식을 세워 문제를 해결
"""