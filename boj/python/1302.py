if __name__ == "__main__":
    n = int(input())
    sold_list = []
    max = 0
    best_seller = ''
    for i in range(n):
        sold_list.append(str(input()))
    sort_sold_list = sorted(sold_list)
    for i in sort_sold_list:
        if max < sort_sold_list.count(i):
            max = sort_sold_list.count(i)
            best_seller = i
    print(best_seller)
