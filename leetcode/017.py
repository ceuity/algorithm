# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 02:32:36 2021

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_pad = {'2': 'abc', 
                   '3': 'def', 
                   '4': 'ghi', 
                   '5': 'jkl', 
                   '6': 'mno', 
                   '7': 'pqrs', 
                   '8': 'tuv',
                   '9': 'wxyz'}
        digit_list = []
        for digit in digits:
            digit_list.append(num_pad[digit])
        answer = []
        while digit_list:
            if not answer:
                alphas = digit_list.pop(0)
                for alpha in alphas:
                    answer.append(alpha)
            else:
                alphas = digit_list.pop(0)
                temp = []
                for prev in answer:
                    for alpha in alphas:
                        temp.append(prev+alpha)
                answer = temp
        return answer
        
digits = "234"
ret = Solution()
print(ret.letterCombinations(digits))
