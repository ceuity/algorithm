# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 22:34:20 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder:
            root_index = inorder.index(preorder.pop(0))
            
            node = TreeNode(inorder[root_index])
            node.left = self.buildTree(preorder, inorder[:root_index])
            node.right = self.buildTree(preorder, inorder[root_index + 1:])
            
            return node
        
    
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
ret = Solution()
ret.buildTree(preorder, inorder)

"""
트리의 순회 결과 두 가지가 있으면 트리를 복원할 수 있다.
해당 규칙을 이용하여 분할 정복을 이용하여 문제를 해결한다.
"""