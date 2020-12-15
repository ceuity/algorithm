import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    num_list = [0] * 10001
    for i in range(n):
        num_list[int(sys.stdin.readline())] += 1
    for i in range(10001):
        while num_list[i] != 0:
            print(i)
            num_list[i] -= 1