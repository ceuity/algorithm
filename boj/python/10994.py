if __name__ == "__main__":
    n = int(input())
    temp = (4 * n) - 3
    sum = 0
    for i in range(temp):
        if i % 2 == 0:
            for j in range(sum):
                if j % 2 == 0:
                    print('*', end='')
                else:
                    print(' ', end='')
            for j in range(temp - (sum * 2)):
                print('*', end='')
            for j in range(sum):
                if j % 2 == 0:
                    print(' ', end='')
                else:
                    print('*', end='')
        if i % 2 == 1:
            for j in range(sum):
                if j % 2 == 0:
                    print('*', end='')
                else:
                    print(' ', end='')
            for j in range(temp - (sum * 2)):
                print(' ', end='')
            for j in range(sum):
                if j % 2 == 0:
                    print('*', end='')
                else:
                    print(' ', end='')

        if i >= temp // 2:
            sum -= 1
        else:
            sum += 1
        print('')