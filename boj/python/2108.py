import sys
from collections import Counter


if __name__ == "__main__":
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(sys.stdin.readline()))
    # 산술평균
    nums.sort()
    print(round((sum(nums) / len(nums))))
    # 중앙값
    print(nums[len(nums) // 2])
    # 최빈값
    mode = Counter(nums)
    if len(nums) > 1 and mode.most_common(2)[0][1] == mode.most_common(2)[1][1]:
        print(Counter(nums).most_common(2)[1][0])
    else:
        print(Counter(nums).most_common(1)[0][0])
    # 범위
    print(max(nums) - min(nums))
