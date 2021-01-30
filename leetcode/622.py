# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 02:08:53 2021

"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = collections.deque()
        self.length = k

    def enQueue(self, value: int) -> bool:
        if len(self.q) < self.length:
            self.q.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.q:
            return False
        else:
            self.q.popleft()
            return True

    def Front(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1
        
    def Rear(self) -> int:
        if self.q:
            return self.q[-1]
        else:
            return -1
            
    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.length


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

"""
이 문제는 원형 큐를 디자인하는 문제이다. 원형 큐를 구현하는 방법에는 다양한 방법이 있으나,
이 문제는 deque를 이용하여 풀었다. 원형으로 구현해야한다고는 하나 실제로 deque를 이용하면
원형으로 구현하지 않아도 문제를 해결할 수 있다.
"""