from math import factorial

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(factorial(N) // (factorial(K) * factorial(N - K)))