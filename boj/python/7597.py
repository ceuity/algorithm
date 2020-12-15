if __name__ == "__main__":
    while True:
        user_input = str(input())
        if user_input == '#':
            break
        score_A = 0
        score_B = 0
        win_A = 0
        win_B = 0
        for i in range(len(user_input)):
            if user_input[i] == 'A':
                score_A += 1
            elif user_input[i] == 'B':
                score_B += 1
            if score_A >= 4 and score_A - score_B >= 2:
                win_A += 1
                score_A = 0
                score_B = 0
            elif score_B >= 4 and score_B - score_A >= 2:
                win_B += 1
                score_A = 0
                score_B = 0
        print('A', win_A, 'B', win_B)