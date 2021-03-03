# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:47:37 2021

"""

if __name__ == "__main__":
    coins = [500, 100, 50, 10, 5, 1]
    answer = 0
    otsuri = 1000 - int(input())
    for coin in coins:
        answer += otsuri // coin
        otsuri = otsuri % coin
    print(answer)
    
"""
전형적인 그리디 알고리즘 문제
거스름돈을 동전의 금액으로 나눈 몫이 동전의 갯수고, 나머지가 다음 동전으로 나눠야할 수가 된다.
"""