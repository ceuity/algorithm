import sys


if __name__ == "__main__":
    n = int(input())
    stack = []
    answer = []
    nums = 1
    for _ in range(n):
        input_num = int(sys.stdin.readline())
        while nums <= input_num:
            stack.append(nums)
            answer.append("+")
            nums += 1
        if stack.pop() == input_num:
            answer.append("-")
        else:
            print("NO")
            exit()
    print('\n'.join(answer))
