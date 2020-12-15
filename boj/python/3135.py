if __name__ == "__main__":
    src, dest = map(int, input().split())
    fav = int(input())
    fav_list = []
    count = 0
    temp = 0
    min = abs(src - dest)
    for i in range(fav):
        fav_list.append(int(input()))
    for i in fav_list:
        if abs(i - dest) < min:
            min= abs(i - dest)
            temp = i
    if min < abs(src - dest):
        count += 1 + abs(temp - dest)
    else:
        count += abs(src - dest)
    print(count)