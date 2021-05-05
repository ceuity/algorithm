from collections import deque
from typing import List

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         answer = []
#         window = deque()
#         num_max = float('-inf')
#         for i, num in enumerate(nums):
#             window.append(num)
#             if i < k - 1:
#                 continue
#             elif i == k - 1:
#                 num_max = max(window)
#             if nums[i] > num_max:
#                 num_max = nums[i]
#             answer.append(num_max)
#             if num_max == window.popleft():
#                 num_max = float('-inf')
#
#         return answer


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_q = deque()
        ans = []
        for i in range(n):
            while max_q and nums[max_q[-1]] < nums[i]:
                max_q.pop()
            max_q.append(i)

            if max_q[0] == i - k:
                max_q.popleft()

            if i + 1 >= k:
                ans.append(nums[max_q[0]])

        return ans


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    ret = Solution()
    print(ret.maxSlidingWindow(nums, k))

"""
기존에 책에 있는 방법은 모두 시간초과가 났다. 아마 테스트케이스가 더 추가된 것 같다.
최댓값의 인덱스를 저장하는 방법으로 풀어야 풀 수 있었다.
"""