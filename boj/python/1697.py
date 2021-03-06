# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 04:49:04 2021

"""

from collections import deque

if __name__ == '__main__':
    start, target = map(int, input().split())
    count = 0
    q = deque([start])
    visited = [0] * 100001
    
    while q:
        for _ in range(len(q)): 
            curr = q.popleft()
            if not visited[curr]:
                visited[curr] = 1
                if curr == target:
                    break
                if curr - 1 >= 0:
                    q.append(curr - 1)
                if curr + 1 <= 100000:
                    q.append(curr + 1)
                if curr * 2 <= 100000:
                    q.append(curr * 2)
        if curr == target:
            break
        count += 1
    print(count)
   
"""
처음에 visited = [] 로 선언하고 방문할 때 마다 visited에 있는지 확인 후 추가해줬더니 시간초과가 났다.
아무래도 visited를 확인하는 과정에서 O(N) 만큼이 더 걸리기 때문인 것 같아서 visited를 미리 선언해주었다.
"""