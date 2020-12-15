def CheckBingo(bingo):
    bingo_count = 0
    for i in range(5):
        if bingo[i][i] != 0:
            break
        if i == 4:
            bingo_count += 1
    for i in range(5):
        if bingo[i][4 - i] != 0:
           break
        if i == 4:
            bingo_count += 1
    for i in range(5):
        for j in range(5):
            if bingo[i][j] != 0:
               break
            if j == 4:
                bingo_count += 1
    for i in range(5):
        for j in range(5):
            if bingo[j][i] != 0:
                break
            if j == 4:
                bingo_count += 1
    return bingo_count

if __name__ == "__main__":
    bingo = []
    call_list = []
    count = 0
    x, y = 0, 0
    for i in range(5):
        bingo.append(list(map(int, input().split())))
    for i in range(5):
        call_list.extend(list(map(int, input().split())))
    for number in call_list:
        count += 1
        for i in bingo:
            if number in i:
                x = i.index(number)
                y = bingo.index(i)
                bingo[y][x] = 0
                break
        if CheckBingo(bingo) >= 3:
            print(count)
            break