class Solution:
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))


"""
이전에 프로그래머스에서 풀었던 경험이 있어서 해당 문제를 찾아보았으나,
프로그래머스에서의 문제가 훨씬 제한 조건이 덜 까다로운 문제여서 당시의 방법으로는 풀리지 않았다.
cmp_to_key 를 이용하여 푸는 방법도 있었다.
"""