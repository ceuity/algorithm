# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:16:39 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            count += 1
        return count
    
"""
BFS를 이용하면 쉽게 풀 수 있다.
"""