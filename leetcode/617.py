# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 02:20:56 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node
        else:
            return root1 or root2

"""
아직 재귀에 익숙하지 않은 것 같다. 로직 자체는 구현할 수 있는데 그걸 코드로 옮기는 게 잘 안된다.
"""