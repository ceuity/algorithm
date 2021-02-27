# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 22:12:15 2021

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 둘 다 빈 리스트일 때
        if not l1 and not l2:
            return None
        merge_list = ListNode()
        # curr = 현재 List 위치
        curr = merge_list
        while l1 or l2:
            if not l1:
                curr.val = l2.val
                l2 = l2.next
            elif not l2:
                curr.val = l1.val
                l1 = l1.next
            elif l1.val > l2.val:
                curr.val = l2.val
                l2 = l2.next
            elif l1.val <= l2.val:
                curr.val = l1.val
                l1 = l1.next
            if l1 or l2:
                curr.next = ListNode()
                curr = curr.next
        return merge_list
    
"""
python에서 Linked list를 쓰는 게 익숙하지 않아서 조금 시간이 걸렸다.
정말 정석적인 방법으로 l1, l2의 val을 비교해서 더 큰 쪽을 merge_list.val로 하고
merge_list.next를 새로 생성해준 후 다음 list로 이동하였다.
"""