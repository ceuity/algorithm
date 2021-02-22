# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:36:19 2020

@author: EVer
"""

from collections import Counter
from operator import itemgetter

def solution(genres, plays):
    play_count = {}
    zip_list = []
    answer = []
    for z in zip(range(len(genres)), genres, plays):
        zip_list.append(list(z))
    for c in zip_list:
        if c[1] not in play_count:
            play_count[c[1]] = c[2]
        else:
            play_count[c[1]] += c[2]
    genre_rank = list(map(lambda x: x[0], sorted(play_count.items(), key=itemgetter(1), reverse=True)))
    for rank in genre_rank:
        temp = []
        for index, genre, count in zip_list:
            if genre == rank:
                temp.append([index, count])
        temp = sorted(temp, key=lambda x:x[1], reverse=True)
        temp = temp[:2]
        for t in temp:
            answer.append(t[0])
    return answer
    

genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'classic', 'pop', 'classic', 'rock', 'jazz']
plays = [500, 600, 150, 800, 2500, 500, 600, 150, 800, 3000]
solution(genres, plays)
