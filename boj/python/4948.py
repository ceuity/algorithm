def isPrime(num):
    if num == 1:
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True

if __name__ == "__main__":
    total_list = list(range(2, 246913))
    prime_list = []
    for k in total_list:
        if isPrime(k) is True:
            prime_list.append(k)
    while True:
        n = int(input())
        if n == False:
            break
        count = 0
        for i in prime_list:
            if n < i and i <= 2 * n:
                count += 1
        print(count)
