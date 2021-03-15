# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 00:08:34 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.longest = max(self.longest, left + right)
            
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
    
"""
BFS를 이용하여 현재 위치에서 깊이를 구한 후 양쪽을 더하는 방법으로 시도했었는데,
일부 테스트케이스가 정상 동작하지 않는 걸 발견하여 DFS로 변경하였다.
항상 longest와 같은 변수를 어떻게 선언해주어야 하나 고민이었는데 class 변수로 선언하는 게 좋은 것 같다.
"""