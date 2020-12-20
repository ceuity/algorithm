# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 02:44:55 2020

@author: EVer
"""

class queue:
    
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        self.items.pop()
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
