# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 23:10:00 2021

"""

if __name__=="__main__":
    n = int(input())
    dict = {}
    dict[0] = 0
    dict[1] = 0
    for i in range(2, n + 1):
        if i % 6 == 0:
            if i not in dict:
                dict[i] = min(dict[i // 2], dict[i // 3]) + 1
        elif i % 2 == 0:
            if i not in dict:
                dict[i] = min(dict[i // 2], dict[i - 1]) + 1
        elif i % 3 == 0:
            if i not in dict:
                dict[i] = min(dict[i // 3], dict[i - 1]) + 1
        else:
            if i not in dict:
                dict[i] = dict[i - 1] + 1
    print(dict[n])
    
"""
다음 수를 구할 떄 이전 연산에 필요했던 수를 저장해두었다가 더 작은 값을 사용하여 문제를 해결였다.
"""