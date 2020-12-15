if __name__ == "__main__":
    n = int(input())
    count = 0
    while True:
        count += 1
        if str(count).count('666'):
            n -= 1
        if n == 0:
            print(count)
            break