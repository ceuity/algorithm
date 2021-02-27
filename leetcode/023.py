# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 23:51:08 2021

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        temp = head
        stack = []
        for i in lists:
            while i:
                stack.append(i)
                i = i.next
        stack = sorted(stack, key=lambda x:x.val, reverse=True)
        while stack:
            temp.next = stack.pop()
            temp = temp.next
        temp.next = None
        return head.next
    
"""
처음에는 기존의 linked list의 next를 연결하는 방식으로 하려고 했었다가
잘 되지 않는 것 같아서 linked list를 모두 stack에 넣은 후 value값을 기준으로
정렬하여 linked list로 다시 연결시켜주었다.
"""