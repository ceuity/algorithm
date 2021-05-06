# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         t_dict = {}
#         min_subs = float('inf')
#         answer = ''
#         for i in range(len(s)):
#             if s[i] in t:
#                 t_dict[s[i]] = i
#             if len(t) == len(t_dict):
#                 if not answer:
#                     answer = s[min(t_dict.values()):max(t_dict.values())+1]
#                 elif len(answer) > max(t_dict.values()) - min(t_dict.values()) + 1:
#                     answer = s[min(t_dict.values()):max(t_dict.values())+1]
#         return answer

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letter_counter = collections.Counter(t)
        missing = len(t)
        start = end = left = 0

        for right, char in enumerate(s, 1):
            if letter_counter[char] > 0:
                missing -= 1
            letter_counter[char] -= 1

            if missing == 0:
                while left < right and letter_counter[s[left]] < 0:
                    letter_counter[s[left]] += 1
                    left += 1
                if not end or right - left < end - start:
                    start, end = left, right
                missing += 1
                letter_counter[s[left]] += 1
                left += 1

        return s[start:end]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    ret = Solution()
    print(ret.minWindow(s, t))