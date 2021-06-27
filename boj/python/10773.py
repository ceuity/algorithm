import sys

if __name__ == "__main__":
    K = int(input())
    nums = []
    for _ in range(K):
        num = int(sys.stdin.readline())
        if num == 0:
            nums.pop()
        else:
            nums.append(num)
    print(sum(nums))