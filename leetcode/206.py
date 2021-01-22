# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 02:07:22 2021

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None # 첫 Linked List 생성
        # head List의 끝까지 탐색
        while head:
            temp = ListNode()
            temp.val = head.val
            temp.next = prev
            prev = temp
            head = head.next
        return prev

"""
이 문제는 새로운 Linked list를 만들고, 입력받은 Linked list를 하나씩 지나가면서
새로운 Linked list에 역순으로 연결되게 하였다.
"""
