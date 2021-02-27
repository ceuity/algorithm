# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 02:15:01 2021

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_list = ListNode()
        curr = sum_list
        while l1 or l2:
            if not l1:
                remain_val = (curr.val + l2.val) // 10
                curr.val = (curr.val + l2.val) % 10
                l2 = l2.next
            elif not l2:
                remain_val = (curr.val + l1.val) // 10
                curr.val = (curr.val + l1.val) % 10
                l1 = l1.next
            else:
                remain_val = (curr.val + l1.val + l2.val) // 10
                curr.val = (curr.val + l1.val + l2.val) % 10
                l1 = l1.next
                l2 = l2.next
            if l1 or l2:
                curr.next = ListNode()
                curr = curr.next
                curr.val = remain_val
        # 마지막 자릿수 확인
        if remain_val == 1:
                curr.next = ListNode()
                curr = curr.next
                curr.val = remain_val
        return sum_list
    
"""
이 문제는 간단하게 생각하면 두 Linked list의 val을 더해서 새로운 sum_list를
만들어주면 되는 문제이다. 대신 합계가 10이 넘을 경우에는 다음 리스트로 넘겨주어야
하기 때문에 while문 마지막에 l1.val과 l2.val을 더해서 10으로 나눈 나머지를
다음 리스트의 val에 미리 더해주었다.

다른 사람들의 풀이를 보니 l1과 l2가 존재할 때를 먼저 계산하고
그 다음 l1이 존재할 때, l2가 존재할 때 두 경우를 모두 처리해주는 방식이
조금 더 읽기 쉬운 방법인 것 같다.
"""