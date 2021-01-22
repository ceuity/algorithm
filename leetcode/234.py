# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:39:31 2021

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val_list = []
        curr = head
        while curr:
            val_list.append(curr.val)
            curr = curr.next
        return val_list == val_list[::-1]

"""
Linked list를 순회하면서 val값을 val_list에 저장해서
val_list가 Palindrome인지 확인하였다.
"""