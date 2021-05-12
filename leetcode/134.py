from typing import List

# class Solution:
#     def check_gas(self, start, gas, cost):
#         if gas[start] < cost[start]:
#             return False
#         fuel = 0
#         for i in range(len(gas)):
#             fuel += gas[(start + i) % len(gas)]
#             if fuel - cost[(start + i) % len(gas)] < 0:
#                 return False
#         return True
#
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         for i in range(len(gas)):
#             if self.check_gas(i, gas, cost):
#                 return i
#         return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        fuel = 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start

if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    ret = Solution()
    print(ret.canCompleteCircuit(gas, cost))

"""
해가 오직 하나만 존재하여 가능한 풀이. 앞의 조건이 불가하면 다음 조건으로 넘어간다.
"""