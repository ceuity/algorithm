# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 02:39:58 2021

"""

def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        answer += 1
    return answer

"""
문제 조건 까먹고 있다가 여러명인 경우 생각해서 풀려고 했더니 복잡해져서 풀이를 확인했더니
2명 제한이 있었다...... 나는 멍청이다......
처음부터 투포인터로 풀어야 할 것 같았는데 괜히 다른 방법 써보려다가 시간만 날렸다.
"""