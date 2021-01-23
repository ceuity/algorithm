# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:53:04 2021

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Linked list가 존재하지 않을 때 예외처리
        if not head:
            return None
        odd = head
        even_head = head.next
        even = even_head
        # even의 next가 없으면 list의 끝
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        # odd의 다음은 even의 시작
        odd.next = even_head
        return head
    
"""
이 문제는 Linked list를 홀수번과 짝수번을 나눠서 정렬시키는 문제이다.
처음에는 노드를 swap해야 하나 싶었는데 다시 생각해보니 홀수, 짝수번째의 Node만 이어서
홀수번째 마지막을 짝수번째 시작 노드에 연결해주면 되는 문제였다.
"""