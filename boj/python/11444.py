from collections import defaultdict


# 행렬 곱 계산
def matrix_mul(x, y):
    a = x[0][0] * y[0][0] + x[0][1] * y[1][0]
    b = x[0][0] * y[0][1] + x[0][1] * y[1][1]
    c = x[1][0] * y[0][0] + x[1][1] * y[1][0]
    d = x[1][0] * y[0][1] + x[1][1] * y[1][1]

    return [[a % mod, b % mod], [c % mod, d % mod]]


# 피보나치 분할 정복
def fibonacci(matrix, n):
    if n == 1:
        return fibo_dict[n]
    if n % 2 == 0:
        if not fibo_dict[n]:
            fibo_dict[n] = matrix_mul(fibonacci(matrix, n // 2), fibonacci(matrix, n // 2))
        return fibo_dict[n]
    else:
        if not fibo_dict[n]:
            fibo_dict[n] = matrix_mul(fibonacci(matrix, n - 1), fibonacci(matrix, 1))
        return fibo_dict[n]


if __name__ == "__main__":
    n = int(input())
    mod = 1000000007
    base_matrix = [[1, 1], [1, 0]]
    fibo_dict = defaultdict(list)
    fibo_dict[1] = base_matrix
    print(fibonacci(base_matrix, n)[0][1] % 1000000007)
