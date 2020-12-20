# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 00:33:52 2020

@author: EVer
"""

def solution(begin, target, words):
    if target not in words:
        return 0
    queue = [begin]
    total_count = 0
    while len(words) != 0:
        for value in queue:
            temp = []
            for word in words:
                count = 0
                for i in range(len(word)):
                    if value[i] != word[i]:
                        count += 1
                    if count == 2:
                        break
                if count == 1:
                    temp.append(word)
                    words.remove(word)
        total_count += 1
        if len(temp) == 1 and target == temp[0]:
            return total_count
        else:
            queue = temp
    return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))