# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 00:27:33 2021

"""

""" Time Limit Exceeded
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        answer = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    pal = words[i] + words[j]
                    if pal == pal[::-1]:
                        answer.append([i, j])
        return answer
"""
from typing import List
from collections import defaultdict

""" 972ms
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_word_ids = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]
        
    # 단어 삽입
    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index
    
    def search(self, index, word):
        result = []
        node = self.root
        
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
            
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        
        return result
    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        
        for i, word in enumerate(words):
            trie.insert(i, word)
            
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
            
        return results
"""

# 360ms

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        rev_dict = defaultdict(int)
        # reversed word dictionary
        for i, v in enumerate(words):
            rev_dict[v[::-1]] = i
        index = set()
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                if prefix in rev_dict and i != rev_dict[prefix] and suffix[::-1] == suffix:
                    index.add((i, rev_dict[prefix]))
                if suffix in rev_dict and i != rev_dict[suffix] and prefix == prefix[::-1]:
                    index.add((rev_dict[suffix], i))
        return [list(i) for i in index]

if __name__ == '__main__':
    words = ["abcd","dcba","lls","s","sssll"]
    ret = Solution()
    ret.palindromePairs(words)


"""
Trie 구조로 만들어서 푸는 방법이 정석적인 방법인 것 같지만 속도는 더 느렸다.
prefix와 suffix로 분리했을 때, prefix 또는 suffix가 reversed_dict에 들어있고, 남은 부분이 palindrome이면,
해당 pair는 palindrome pair이다.
"""