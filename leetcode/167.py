class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif target - numbers[left] < numbers[right]:
                right -= 1
            else:
                left += 1

"""
처음에 2중 for문으로 풀이했었는데 시간 초과가 나서 two pointer 방법으로 변경하였다.
"""