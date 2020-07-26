import sys

def mergeSort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left_list = list[:mid]
    right_list = list[mid:]
    left_list = mergeSort(left_list)
    right_list = mergeSort(right_list)
    return merge(left_list, right_list)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

if __name__ == "__main__":
    ipt = sys.stdin.readline
    n = int(ipt())
    number_list = []
    for i in range(n):
        number_list.append(int(ipt()))
    res = mergeSort(number_list)
    for j in res:
        print(j)