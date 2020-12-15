import itertools

if __name__ == "__main__":
    arr_list = []
    n = 9
    while n > 0:
        arr_list.append(int(input()))
        n -= 1
    arr_list.sort()
    answer_list = list(itertools.combinations(arr_list, 7))
    for i in answer_list:
        answer = 0
        for j in i:
            answer += j
        if answer == 100:
            for j in i:
                print(j)
            break