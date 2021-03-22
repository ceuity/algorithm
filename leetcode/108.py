# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 23:34:38 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return node
    
"""
균형 이진 트리를 만드는 문제이다.
이진 탐색하는 방법을 역으로 이용하여 이진 트리를 만들었다.
"""