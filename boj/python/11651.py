from operator import itemgetter

if __name__ == '__main__':
    n = int(input())
    xy_list = []
    for i in range(n):
        xy_list.append(list(map(int, input().split())))
    xy_sort_list = sorted(xy_list, key=itemgetter(1, 0))
    for j in xy_sort_list:
        print(j[0], j[1])
