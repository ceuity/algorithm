# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:30:22 2021

"""

from collections import deque

if __name__ == '__main__':
	k = int(input())
	if k == 0:
		print(0)
		exit()
	dx = [1, 1, -1, -1, 2, 2, -2, -2]
	dy = [2, -2, 2, -2, 1, -1, 1, -1]

	def bfs():
		n = int(input())
		grid = [[0 for _ in range(n)] for _ in range(n)]
		s_x, s_y = map(int, input().split())
		t_x, t_y = map(int, input().split())
		q = deque([[s_x, s_y]])
		while q:
			ax, ay = q.popleft()
			if ax == t_x and ay == t_y:
				return grid[ay][ax]
			for i in range(8):
				x = ax + dx[i]
				y = ay + dy[i]
				if 0 <= x < n and 0 <= y < n and grid[y][x] == 0:
					grid[y][x] = grid[ay][ax] + 1
					q.append([x, y])
		return -1

	for _ in range(k):
		print(bfs())

"""
확실히 문제를 풀다보니 +- 1씩 해주는 부분은 dx, dy를 정의해서 더해주는 쪽이 더 깔끔한 코드가 되는 것 같다.
순서를 [x, y]로 할지, [y, x]로 할지 확실하게 정해서 헷갈리지 않도록 하자. 
"""