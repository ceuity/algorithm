from typing import List
import heapq

# class Solution:
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         heap = []
#         for person in people:
#             heapq.heappush(heap, [-person[0], person[1]])
#
#         result = []
#         while heap:
#             person = heapq.heappop(heap)
#             result.insert(person[1], [-person[0], person[1]])
#         return result

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        ans = []
        for p in people:
            ans.insert(p[1], p)

        return ans

if __name__ == "__main__":
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ret = Solution()
    print(ret.reconstructQueue(people))

"""
그리디 문제는 확실히 많이 풀어볼 수록 유형이 보여서 안 풀어본 문제는 해답을 찾기 어려운 것 같다.
"""