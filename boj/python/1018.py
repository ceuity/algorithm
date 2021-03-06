# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 02:54:23 2021

"""

if __name__=='__main__':
    m, n = map(int, input().split())
    full_grid = []
    min_count = float('inf')
    for _ in range(m):
        full_grid.append(input())

    def find_counts(c1, c2, grid):
        count = 0
        for i, row in enumerate(grid):
            if i % 2 == 0:
                for j in range(len(row)):
                    if j % 2 == 0:
                        if row[j] != c1:
                            count += 1
                    else:
                        if row[j] != c2:
                            count += 1
            else:
                for j in range(len(row)):
                    if j % 2 == 0:
                        if row[j] != c2:
                            count += 1
                    else:
                        if row[j] != c1:
                            count += 1
        return count

    for i in range(m - 7):
        for j in range(n - 7):
            sub_grid = list(map(lambda x: x[j:j+8], full_grid[i:i+8]))
            min_count = min(min_count, find_counts('B', 'W', sub_grid))
            min_count = min(min_count, find_counts('W', 'B', sub_grid))
    print(min_count)

"""
백트래킹으로 다 찾아보자
"""