if __name__ == "__main__":
    n, k = map(int, input().split())
    num_list = []
    answer = []
    for i in range(1, n + 1):
        num_list.append(i)
    popNum = 0
    while num_list:
        popNum = (popNum + (k - 1)) % len(num_list)
        answer.append(str(num_list.pop(popNum)))
    print("<%s>" %(", ".join(answer)))