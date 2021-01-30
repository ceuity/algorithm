# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 01:51:22 2021

"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
이 문제는 225번 문제와는 반대로 queue를 이용하여 stack을 구현하는 문제이다.
stack에 넣을 때 queue의 순서를 유지할 수 있도록 기존에 있는 stack을 임시로 전부 pop한 후,
기존의 stack에 새로 추가할 요소를 먼저 push한 후에 다시 임시 stack에 있는 요소들을
기존의 stack으로 옮기는 방식을 사용하였다.
"""