if __name__ == '__main__':
    prime_min = int(input())
    prime_max = int(input())
    prime_list = []
    prime_sum = 0
    flag = 0
    for i in range(prime_min, prime_max + 1):
        if i == 1:
            continue
        for j in range(1, i + 1):
            if flag > 2:
                break
            elif i % j == 0:
                flag += 1
        if flag == 2:
            prime_list.append(i)
        flag = 0
    for k in prime_list:
        prime_sum = prime_sum + k
    if bool(prime_list):
        print(prime_sum)
        print(prime_list[0])
    else:
        print("-1")
