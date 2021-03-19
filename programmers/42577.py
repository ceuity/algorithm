# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:15:53 2020

@author: EVer
"""
""" 테스트 케이스가 바뀌어 아래 코드는 더이상 통과할 수 없었다.
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].find(phone_book[i]) == 0:
                print(phone_book[j].find(phone_book[i]))
                return False
    answer = True
    return answer
"""

def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]
    print(solution(phone_book))