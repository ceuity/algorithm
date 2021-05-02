from math import factorial


def solution():
    n, m = map(int, input().split())
    print(factorial(n) // (factorial(m) * factorial(n-m)))

if __name__ == "__main__":
    solution()