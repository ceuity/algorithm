# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        root = ListNode()
        curr = root
        while head:
            while curr.next and curr.next.val < head.val:
                curr = curr.next

            temp = head.next
            head.next = curr.next
            curr.next = head
            head = temp

            # curr.next, head.next, head = head, curr.next, head.next
            if head and curr.next.val > head.val:
                curr = root
        return root.next

"""
파이썬 다중 할당 연산자를 이용하면 temp을 사용하지 않아도 할당 시의 값을 기억하여 한 줄로 쓸 수 있다.
"""