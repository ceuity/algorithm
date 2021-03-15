# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 01:03:29 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 파이썬 다운 방식
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0
            node.left, node.right = node.right, node.left
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return root
    
    
# temp을 이용한 swap
"""    
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0
            
            temp = node.left
            node.left = node.right
            node.right = temp
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return root
"""

# 반복 구조로 BFS
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                queue.append(node.right)
                
        return root
"""

# 반복 구조로 DFS
"""    
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = deque([root])
        
        while queue:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                
                stack.append(node.left)
                stack.append(node.right)
                
        return root
"""

# 반복 구조로 DFS 후위 순회
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = deque([root])
        
        while queue:
            node = stack.pop()
            
            if node:
                stack.append(node.left)
                stack.append(node.right)
                
                node.left, node.right = node.right, node.left
                
        return root
"""

"""
C에서 포인터의 개념을 알고 있으면 어렵지 않게 풀 수 있는 문제인 것 같다.
node도 결국엔 하나의 주소값이기 때문에 주소값만 잘 바꿔주면 쉽게 풀린다.
"""