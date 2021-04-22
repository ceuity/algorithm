from collections import defaultdict
import sys

if __name__ == "__main__":
    M, N = map(int, input().split())
    poke2num = defaultdict(int)
    num2poke = defaultdict(str)
    for i in range(1, M+1):
        name = str(sys.stdin.readline().strip())
        poke2num[name] = i
        num2poke[i] = name
    for _ in range(N):
        ans = sys.stdin.readline().strip()
        try:
            ans = int(ans)
            print(num2poke[ans])
        except ValueError:
            print(poke2num[ans])