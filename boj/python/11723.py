import sys


def solution():
    M = int(input())
    _set = set()
    for _ in range(M):
        temp = sys.stdin.readline().strip().split()
        if len(temp) == 1:
            cmd = temp[0]
        else:
            cmd = temp[0]
            num = int(temp[1])

        if cmd == 'add':
            _set.add(num)
        elif cmd == 'remove':
            if num in _set:
                _set.discard(num)
        elif cmd == 'check':
            if num in _set:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if num in _set:
                _set.discard(num)
            else:
                _set.add(num)
        elif cmd == 'all':
            _set = set([i for i in range(1, 21)])
        elif cmd == 'empty':
            _set = set()


if __name__ == "__main__":
    solution()
