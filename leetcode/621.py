from collections import deque, Counter
from typing import List


# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         if n == 0:
#             return len(tasks)
#         answer = 0
#         counts = Counter(tasks)
#
#         while True:
#             sub_count = 0
#             for task, _ in counts.most_common(n + 1):
#                 sub_count += 1
#                 answer += 1
#                 counts.subtract(task)
#                 counts += Counter()
#             if not counts:
#                 break
#             answer += n - sub_count + 1
#
#         return answer

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        longest = max(counter.values())

        ans = (longest - 1) * (n + 1)
        for times in counter.values():
            if times == longest:
                ans += 1
        return max(len(tasks), ans)

if __name__ == "__main__":
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 50
    ret = Solution()
    print(ret.leastInterval(tasks, n))