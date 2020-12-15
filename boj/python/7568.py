if __name__ == "__main__":
    n = int(input())
    body = []
    rank_list = []
    for i in range(n):
        body.append(list(map(int, input().split())))
    for j in body:
        count = 0
        for k in body:
            if j != k:
                if (j[0] < k[0]) and (j[1] < k[1]):
                    count += 1
        rank_list.append(count + 1)
    for l in rank_list:
        print(l, end=" ")