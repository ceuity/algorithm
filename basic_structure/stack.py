# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 02:14:36 2020

@author: EVer
"""

class stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        return self.items.pop()
    
a = stack()

print(a.isEmpty())
print(a.push(1))
print(a.push(2))
print(a.push(3))
print(a.size())
print(a.isEmpty())
print(a.pop())
print(a.pop())
print(a.pop())

