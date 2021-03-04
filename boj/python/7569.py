# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 02:12:54 2021

"""

from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
	m, n, h = map(int, input().split())
	count = -1

	grid = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

	q = deque()

	for z in range(h):
		for y in range(n):
			for x in range(m):
				if grid[z][y][x] == 1:
					q.append([z, y, x])
					grid[z][y][x] = 0

	# def check_grid(z, y, x):
	# 	if z >= 0 and z < h \
	# 		and y >= 0 and y < n \
	# 		and x >= 0 and x < m:
	# 		if grid[z][y][x] == 0:
	# 			return [z, y, x]

	temp = deque()
	# while q:
	# 	z, y, x = q.popleft()
	# 	grid[z][y][x] = 1
	# 	if check_grid(z+1, y, x): temp.append(check_grid(z+1, y, x))
	# 	if check_grid(z-1, y, x): temp.append(check_grid(z-1, y, x))
	# 	if check_grid(z, y+1, x): temp.append(check_grid(z, y+1, x))
	# 	if check_grid(z, y-1, x): temp.append(check_grid(z, y-1, x))
	# 	if check_grid(z, y, x+1): temp.append(check_grid(z, y, x+1))
	# 	if check_grid(z, y, x-1): temp.append(check_grid(z, y, x-1))

	while q:
		z, y, x = q.popleft()
		if 0 <= z < h and 0 <= y < n and 0 <= x < m and grid[z][y][x] == 0:
			grid[z][y][x] = 1
			temp.append([z+1, y, x])
			temp.append([z-1, y, x])
			temp.append([z, y+1, x])
			temp.append([z, y-1, x])
			temp.append([z, y, x+1])
			temp.append([z, y, x-1])

		if not q:
			q = temp
			temp = deque()
			count += 1

	for z in grid:
		for y in z:
			for x in y:
				if x == 0:
					count = 0

	print(count - 1)

"""
처음으로 문제를 풀면서 메모리 초과를 경험해본 문제였다. 메모리는 항상 넉넉한 줄 알았는데 아니었다.
Python3 로 Complie 할 땐 시간 초과지만 PyPy3로 할 땐 메모리 초과였다. 결국 코드를 수정하여 Python3로 통과하였다.
처음 시도했을 땐 grid[z][y][x]에서 z, y, x의 조건을 모두 확인하였는데, 이것이 걸림돌이 되었다.
z, y, x 각 범위를 확인할 때, 각 자리의 조건만 확인하면 시간 초과 문제를 해결할 수 있다.
또한, 해당 z, y, x의 grid가 유효한지 체크하는 함수도 만들었었는데, 이 함수를 들어갔다 나오는 데에도 꽤나 시간이 소요된 것 같다.
"""