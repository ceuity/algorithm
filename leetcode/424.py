# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         maxlen = 0
#         for i in range(len(s)):
#             target = s[i]
#             right = 0
#             replace_count = k
#             while i+right < len(s) and replace_count > 0:
#                 if s[i+right] != target:
#                     replace_count -= 1
#                 right += 1
#             while i+right < len(s) and s[i+right] == target:
#                 right += 1
#             left = 1
#             while i-left >= 0 and replace_count > 0:
#                 if s[i-left] != target:
#                     replace_count -= 1
#                 right += 1
#                 left += 1
#             maxlen = max(maxlen, right)
#         return maxlen

# from collections import Counter

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         left = right = 0
#         counts = Counter(s)
#         for right in range(1, len(s) + 1):
#             counts[s[right - 1]] += 1
#             max_char = counts.most_common(1)[0][1]
#
#             if right - left - max_char > k:
#                 counts[s[left]] -= 1
#                 left += 1
#         return right - left

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k + 1:
            return len(s)

        char_map = defaultdict(int)

        left = 0
        max_char = 0
        max_len = 0

        for right in range(len(s)):
            char_map[s[right]] += 1
            max_char = max(max_char, char_map[s[right]])

            # 바꿀 수 있는 숫자보다 left ~ right의 문자가 더 많은 경우
            if right - left + 1 <= k + max_char:
                max_len = max(max_len, right - left + 1)
            else:
                char_map[s[left]] -= 1
                left += 1

        return max_len

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    ret = Solution()
    print(ret.characterReplacement(s, k))

"""
처음 풀었던 방법은 O(n^2)에 근접한 풀이여서 그런지 시간초과가 났다.
Counter를 이용하거나 hashmap을 이용한 방법이 빠르고 직관적인 것 같다.
"""