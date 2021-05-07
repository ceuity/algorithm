def solution(numbers, hand):
    answer = ''
    prev_left = 10
    prev_right = 10
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            prev_left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            prev_right = number
        else:
            if number == 0:
                number = 11
            left_row = (prev_left - 1) // 3
            left_col = (prev_left - 1) % 3
            right_row = (prev_right - 1) // 3
            right_col = (prev_right - 1) % 3
            target_row = (number - 1) // 3
            target_col = (number - 1) % 3
            left_dist = abs(left_row - target_row) + abs(left_col - target_col)
            right_dist = abs(right_row - target_row) + abs(right_col - target_col)
            if left_dist > right_dist:
                answer += 'R'
                prev_right = number
            elif left_dist < right_dist:
                answer += 'L'
                prev_left = number
            else:
                if hand == 'right':
                    answer += 'R'
                    prev_right = number
                else:
                    answer += 'L'
                    prev_left = number

    return answer

if __name__ == "__main__":
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = 'left'
    print(solution(numbers, hand))