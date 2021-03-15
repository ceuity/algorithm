# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 02:18:07 2021

"""

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    sums = -1001
    ans = -1001
    for num in nums:
        if num >= 0 and sums >= 0:
            sums += num
        elif num >= 0 and sums < 0:
            sums = num
        elif num < 0:
            if sums + num > 0:
                ans = max(ans, sums)
                sums += num
            else:
                ans = max(ans, sums)
                sums = num
    ans = max(ans, sums)
    print(ans)
    
"""
음수를 기준으로 최댓값이랑 비교하여 값을 갱신한 후, 이전까지 더한 수가 음수값보다 크면 더하고,
아니면 음수값을 다시 합계로 초기화하고 덧셈을 하는 방식으로 문제를 해결하였다.
"""