# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 01:13:46 2021

"""

class MyHashMap:

    def __init__(self):
        self.hash = {}
        
    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            self.hash[key] = value
        else:
            self.hash[key] = value
        
    def get(self, key: int) -> int:
        if key in self.hash:
            return self.hash[key]
        else:
            return -1
        
    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
이 문제는 기본적인 key, value 구조를 가지는 hash table을 만들어보는 문제이다.
hash table의 구조를 생각하면서 주어진 조건에 맞게 작성하였다.
"""