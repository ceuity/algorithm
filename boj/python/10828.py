import sys

if __name__ == "__main__":

    N = int(input())
    stack = []
    for _ in range(N):
        cmd = sys.stdin.readline().split()
        if cmd[0] == 'push':
            stack.append(cmd[1])
        elif cmd[0] == 'pop':
            print(stack.pop()) if stack else print(-1)
        elif cmd[0] == 'size':
            print(len(stack))
        elif cmd[0] == 'empty':
            print(0) if stack else print(1)
        elif cmd[0] == 'top':
            print(stack[-1]) if stack else print(-1)
        else:
            continue