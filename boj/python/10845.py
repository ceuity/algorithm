from collections import deque
import sys

if __name__ == "__main__":
    N = int(input())
    queue = deque()
    for _ in range(N):
        cmd = sys.stdin.readline().split()
        if cmd[0] == 'push':
            queue.append(cmd[1])
        elif cmd[0] == 'pop':
            print(queue.popleft()) if queue else print(-1)
        elif cmd[0] == 'size':
            print(len(queue))
        elif cmd[0] == 'empty':
            print(0) if queue else print(1)
        elif cmd[0] == 'front':
            print(queue[0]) if queue else print(-1)
        elif cmd[0] == 'back':
            print(queue[-1]) if queue else print(-1)
        else:
            continue