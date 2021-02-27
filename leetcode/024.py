# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 03:03:49 2021

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr = prev = head
        while curr and curr.next:
            prec = curr.next
            # head
            if curr == head:
                head = curr.next
                curr.next = head.next
                head.next = curr
            # tail
            elif not curr.next.next:
                prev.next = prec
                curr.next = prec.next
                prec.next = curr
            # mid
            else:
                prev.next = curr.next
                curr.next = prec.next
                prec.next = curr
            prev = curr
            curr = curr.next
        return head

"""
이 문제는 Linked list를 2개씩 짝지어서 swap하는 문제이다.
swap후에는 다음 리스트로 이동하게 되기 때문에 다음 짝을 찾기 위해서는
리스트를 한 칸 더 옮겨주어야 한다.
앞 부분, 중간 부분, 뒷 부분 총 3부분으로 나누어서 각각의 경우에 따라 swap해주었다.
"""