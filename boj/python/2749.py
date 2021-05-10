from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    fibo = defaultdict(int)
    fibo[0] = 0
    fibo[1] = 1
    mod = 1000000
    p = 15 * mod // 10
    for i in range(2, p):
        fibo[i] = fibo[i-1] + fibo[i-2]
        fibo[i] %= mod
    print(fibo[n%p])