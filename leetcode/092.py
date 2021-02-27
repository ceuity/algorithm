# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:39:14 2021

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        root = ListNode()
        root.next = head
        start = root
        for _ in range(m - 1):
            start = start.next
        end = start.next
        for _ in range(n - m):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp
        return root.next
    
"""
이번 문제는 주어진 범위의 list만 reverse하는 문제이다.
처음에는 주어진 범위의 list만 reverse하여 m-1 노드의 next를 rev 노드의 head에 연결하고,
rev 노드의 tail 의 next를 n+1 노드에 연결하려 했지만 잘 되지 않아서 다른 방법을 찾았다.
위 방법은 이동하면서 start의 next를 end의 next로, end의 next를 end의 next.next로
연결하는 방이다.
"""
