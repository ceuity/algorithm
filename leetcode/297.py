# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 04:15:17 2021

"""

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        dq = deque([root])
        answer = ['#']
        while dq:
            curr = dq.popleft()
            if curr:
                answer.append(str(curr.val))
                dq.append(curr.left)
                dq.append(curr.right)
            else:
                answer.append('#')
        while answer[-1] == "null":
            answer.pop()
        return ' '.join(answer)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        data = data.split(' ')
        root = TreeNode(data[1])
        dq = deque([root])
        index = 2
        while dq:
            curr = dq.popleft()
            if data[index] != '#':
                curr.left = TreeNode(data[index])
                dq.append(curr.left)
            index += 1
            if data[index] != '#':
                curr.right = TreeNode(data[index])
                dq.append(curr.right)
            index += 1

        return root
    
"""
index를 0부터 시작했었는데 0은 공백으로 채우고 트리의 index와 data의 index를 일치시키는 것이
더 직관적이고 가독성도 좋은 것 같다.
딱 생각할 수 있는 범위 내에서 문제를 해결할 수 있었다.
"""