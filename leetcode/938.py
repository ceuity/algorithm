# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 00:24:18 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS 재귀 260ms
class Solution:
    val = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        
        if root.val >= low and root.val <= high:
            self.val += root.val
        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)

        return self.val
    
""" 가지치기 192ms
class Solution:    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
"""
    
""" DFS stack 208ms
class Solution:    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        stack = deque([root])
        answer = 0
        while stack:
            curr = stack.pop()
            if curr:
                if curr.val > low:
                    stack.append(curr.left)
                if curr.val < high:
                    stack.append(curr.right)
                if low <= curr.val <= high:
                    answer += curr.val
        return answer
"""

""" BFS 204ms
class Solution:    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        q = deque([root])
        answer = 0
        while q:
            curr = q.popleft()
            if curr:
                if curr.val > low:
                    q.append(curr.left)
                if curr.val < high:
                    q.append(curr.right)
                if low <= curr.val <= high:
                    answer += curr.val
        return answer
"""

"""
기본적으로 모든 노드를 다 탐색하여 해당 값이 low 와 high 범위 사이에 있으면 더하여 값을 return 해주면 된다.
책에서는 가지치기가 가장 빠르다고 되어있으나 실제로 stack을 이용한 DFS나 queue를 이용한 BFS도
범위에 해당하지 않는 값은 제외시켜주기 때문에 속도는 비슷했다.
"""