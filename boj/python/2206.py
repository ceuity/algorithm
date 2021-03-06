# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:10:55 2021

"""

from collections import deque

if __name__ == '__main__':
	n, m = map(int, input().split())
	grid = []
	dx = [1, -1, 0, 0]
	dy = [0, 0, -1, 1]
	for _ in range(n):
		grid.append(list(map(int, input())))
	visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
	q = deque([[0, 0, 1]])
	visited[0][0][1] = 1

	def bfs():
		while q:
			y, x, flag = q.popleft()
			if y == n - 1 and x == m - 1:
				return visited[y][x][flag]
			for i in range(4):
				ax = x + dx[i]
				ay = y + dy[i]
				if 0 <= ax < m and 0 <= ay < n:
					if grid[ay][ax] == 1 and flag == 1:
						visited[ay][ax][0] = visited[y][x][1] + 1
						q.append([ay, ax, 0])
					elif grid[ay][ax] == 0 and visited[ay][ax][flag] == 0:
						visited[ay][ax][flag] = visited[y][x][flag] + 1
						q.append([ay, ax, flag])
		return -1
	print(bfs())

"""
정석적인 bfs 방법으로 풀이하였다. 우선 이동하다가 벽을 만났을 때 flag가 1이면 아직 벽을 부술 수 있는 상태로 벽을 부순다.
이전에는 한 cycle이 모두 같이 진행되기 때문에 count 변수를 사용하여 한 cycle이 돌 때 마다 count 변수를 +1 해주었으나,
이번에는 진행 cycle이 벽을 부쉈을 때와 부수지 않았을 때가 달랐기 때문에 visited에 count를 하도록 해주었다.
grid를 [flag][y][x] 로 했을 땐 오답처리 되었는데 [y][x][flag]순으로 바꾸니까 정답처리 되었다. 원인은 모르겠다.
"""