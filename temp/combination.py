def combination(arr, n):

    def generate(arr_comb):
        if len(arr_comb) == n:
            answer = 0
            for i in arr_comb:
                answer += i
            if answer == 100:
                for num in arr_comb:
                    print(num)
                return

        if arr_comb:
            start = arr.index(arr_comb[-1]) + 1
        else:
            start = 0
        for nxt in range(start, len(arr)):
            arr_comb.append(arr[nxt])
            generate(arr_comb)
            arr_comb.pop()
    generate([])

if __name__ == "__main__":
    arr_list = []
    answer = 0
    n = 9
    while n > 0:
        arr_list.append(int(input()))
        n -= 1
    arr_list.sort()
    combination(arr_list, 7)