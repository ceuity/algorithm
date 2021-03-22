# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 00:14:48 2021

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root
    
"""
이 문제는 node 자신보다 큰 값들의 합으로 트리를 재구성하는 문제이다.
이진 트리가 이미 정렬되어 있기 때문에 자기보다 오른쪽 노드의 합이 node의 값이 된다.
따라서 오른쪽 노드를 먼저 끝까지 탐색하여 끝에서부터 새로운 val 변수에 node의 값을 더하면서 올라온다.
순회 루트는 오른쪽-부모-왼쪽 순이므로 중위 순회 루트와 같다.
"""