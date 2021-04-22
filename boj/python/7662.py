from heapq import heappop, heappush
import sys

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        min_heap, max_heap = [], []
        visited = [False] * 1000001
        N = int(input())
        for i in range(N):
            cmd, n = sys.stdin.readline().rsplit()
            if cmd == 'I':
                heappush(min_heap, (int(n), i))
                heappush(max_heap, (-int(n), i))
                visited[i] = True
            elif cmd == 'D':
                if n == '-1':
                    while min_heap and not visited[min_heap[0][1]]:
                        heappop(min_heap)
                    if min_heap:
                        visited[min_heap[0][1]] = False
                        heappop(min_heap)
                elif n == '1':
                    while max_heap and not visited[max_heap[0][1]]:
                        heappop(max_heap)
                    if max_heap:
                        visited[max_heap[0][1]] = False
                        heappop(max_heap)

        while min_heap and not visited[min_heap[0][1]]:
            heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heappop(max_heap)

        if min_heap and max_heap:
            print(-max_heap[0][0], min_heap[0][0])
        else:
            print("EMPTY")