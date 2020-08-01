if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))
    sort_n_list = sorted(n_list)
    sub_sum = 0
    total_sum = 0
    for i in sort_n_list:
        sub_sum += i
        total_sum += sub_sum
    print(total_sum)