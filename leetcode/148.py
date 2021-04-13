# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        node_list = []
        curr = head
        while curr:
            node_list.append(curr)
            curr = curr.next
        node_list = sorted(node_list, key=lambda x: x.val)
        root = ListNode()
        curr = root
        while node_list:
            curr.next = node_list.pop(0)
            curr = curr.next
        curr.next = None
        return root.next

"""
Linked List를 정렬하는 문제.
각 노드를 순회하면서 value만 저장하여 정렬 후 바꿔주는 방법도 있지만,
노드 자체를 바꿔주는 게 맞다고 생각하여 노드를 바꾸는 방식으로 풀었다.
파이썬은 List에 여러 Object를 담을 수 있기 때문에 위와 같은 풀이가 가능하다.
"""