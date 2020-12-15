if __name__ == '__main__':
    n = int(input())
    prime_list = list(map(int, input().split()))
    count = 0
    flag = 0
    if n == len(prime_list):
        for i in prime_list:
            if i == 1:
                continue
            for j in range(1, i + 1):
                if i % j == 0:
                    flag += 1
            if flag == 2:
                count += 1
            flag = 0
    print(count)
