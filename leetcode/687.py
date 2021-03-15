# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 00:08:39 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
                
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            self.count = max(left + right, self.count)
            return max(left, right)
        
        dfs(root)
        return self.count
    
"""
DFS를 이욯하여 트리의 끝까지 탐색한 후 아래서부터 자식노드와 부모노드의 val이 일치하는지 확인한다.
확인한 후에 left와 right의 합을 count로 다시 갱신하고, 둘 중 큰 값을 return한다.
"""