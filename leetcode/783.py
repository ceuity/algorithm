# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:36:48 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -float('inf')
    answer = float('inf')
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        
        self.answer = min(self.answer, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.answer
    
"""
트리를 중위순회하여 값의 차이가 가장 적은 것을 구하는 문제
"""