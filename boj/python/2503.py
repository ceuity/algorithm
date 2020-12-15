def check_number(test_list, num_list):
    answer = []
    for n in num_list:
        for test in test_list:
            ball_count = 0
            strike_count = 0
            for i in range(3):
                if n[i] == str(test[0])[i]:
                    strike_count += 1
                elif n[i] in str(test[0]):
                    ball_count += 1
            if test[1] != strike_count or test[2] != ball_count:
                break
        if test[1] == strike_count and test[2] == ball_count:
            answer.append(n)
    print(len(answer))

if __name__ == "__main__":
    num_list = []
    n = int(input())
    test_list = []
    for j in range(n):
        test_list.append(list(map(int, input().split())))
    for i in range(123, 1000):
        if str(i)[0] != '0' and str(i)[1] != '0' and str(i)[2] != '0':
            if str(i)[0] != str(i)[1] and str(i)[1] != str(i)[2] and str(i)[2] != str(i)[0]:
                num_list.append(str(i))
    check_number(test_list, num_list)