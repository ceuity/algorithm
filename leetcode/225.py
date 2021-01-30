# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 00:55:46 2021

"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return (self.q.popleft())

    def top(self) -> int:
        """
        Get the top element.
        """
        return (self.q[0])

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.q) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
이 문제는 queue의 작동원리를 이용하여 stack을 구현하는 문제이다.
queue는 FIFO(First In First Out)으로, 먼저 넣은 요소가 먼저 나오게 된다.
stack는 LIFO(Last in First Out)으로, 나중에 넣은 요소가 먼저 나오게 된다.
stack에서는 가장 나중에 넣은 요소가 가장 위에 있기 때문에 마지막에 넣은 요소가
queue에서 가장 앞에 있어야 한다. 따라서 push할 때 기존 queue에 append하고,
append한 요소 앞에 있는 요소들을 queue의 앞에서부터 꺼내어 다시 append 해주어야 한다.
pop을 했을 땐 가장 나중에 넣은 요소를 반환해야 하므로 queue의 0번째 요소를 반환하면 된다.
"""
