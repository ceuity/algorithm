import math

def isPrime(n):
    if n == 1: return False
    k = int(math.sqrt(n))
    for j in range(2, k + 1):
        if n % j == 0:
            return False
    return True

if __name__ == "__main__":
    min, max = map(int, input().split())
    for i in range(min, max + 1):
        if isPrime(i):
            print(i)