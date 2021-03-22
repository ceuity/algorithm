# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:20:23 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def bfs(node):
            q = deque([node])
            count = 0
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr:
                        q.append(curr.left)
                        q.append(curr.right)
                count += 1
            return count
        
        root_q = deque([root])
        while root_q:
            for _ in range(len(root_q)):
                root_node = root_q.popleft()
                if root_node:
                    left = bfs(root_node.left)
                    right = bfs(root_node.right)
                    if abs(left - right) > 1:
                        return False
                    root_q.append(root_node.left)
                    root_q.append(root_node.right)
        return True

"""
재귀로 풀 경우 더 간단하게 풀 수 있다.
재귀로 풀면 시간은 빠르지만 메모리를 더 먹고 큐로 풀면 재귀보단 덜 빠르지만 메모리를 덜 먹는다.
"""