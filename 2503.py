def check_number(test_list, num_list):
    for test in test_list:
        print(test)
        for n in num_list:
            ball_count = 0
            strike_count = 0
            for i in range(3):
                if str(n)[i] == str(test[0])[i]:
                    strike_count += 1
                elif str(n)[i] in str(test):
                    ball_count += 1
            if strike_count != test[1] and ball_count != test[2]:
                num_list.remove(n)
    print(num_list)

if __name__ == "__main__":
    num_list = []
    n = int(input())
    test_list = []
    for j in range(n):
        test_list.append(list(map(int, input().split())))
    for i in range(123, 1000):
        if str(i)[0] != '0' and str(i)[1] != '0' and str(i)[2] != '0':
            if str(i)[0] != str(i)[1] and str(i)[1] != str(i)[2] and str(i)[2] != str(i)[0]:
                num_list.append(i)
    check_number(test_list, num_list)