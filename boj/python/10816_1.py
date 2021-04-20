from collections import Counter

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    target = list(map(int, input().split()))
    arr = Counter(arr)
    answer = []
    for t in target:
        if t in arr:
            answer.append(arr[t])
        else:
            answer.append(0)
    print(' '.join(map(str, answer)))