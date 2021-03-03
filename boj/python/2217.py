# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:16:50 2021

"""

if __name__ == "__main__":
    n = int(input())
    if n == 0:
        print ('0')
        exit
    ropes = []
    temp = []
    answer = 0
    for _ in range(n):
        ropes.append(int(input()))
    ropes.sort(reverse=True)
    for rope in ropes:
        temp.append(rope)
        if temp[-1] * len(temp) > answer:
            answer = temp[-1] * len(temp)
    print(answer)
    
"""
우선 최대로 들 수 있는 무게는 가장 약한 로프를 기준으로 하기 떄문에 가장 약한 로프 * 로프의 갯수이다.
따라서 ropes를 내림차순으로 정렬하여 list에 하나씩 추가하면서 매 순간 버틸 수 있는 무게를 계산하여
최댓값이랑 비교한 후, 더 큰 쪽을 선택한다.
"""