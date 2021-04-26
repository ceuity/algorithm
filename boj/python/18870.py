def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    set_nums = sorted(set(nums))
    nums_dict = {}
    for i, num in enumerate(set_nums):
        nums_dict[num] = i
    answer = []
    for num in nums:
        answer.append(nums_dict[num])
    print(' '.join(map(str, answer)))


if __name__ == "__main__":
    solution()
