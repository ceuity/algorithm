if __name__ == "__main__":
    N, r, c = map(int, input().split())
    answer = 0
    while N > 0:
        temp = (2 ** N) // 2
        if N > 1:
            if r < temp <= c:
                answer += temp ** 2
                c -= temp
            elif r >= temp > c:
                answer += (temp ** 2) * 2
                r -= temp
            elif temp <= r and temp <= c:
                answer += (temp ** 2) * 3
                r -= temp
                c -= temp
        elif N == 1:
            if r == 0 and c == 1:
                answer += 1
            elif r == 1 and c == 0:
                answer += 2
            elif r == 1 and c == 1:
                answer += 3
        N -= 1
    print(answer)
