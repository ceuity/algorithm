import string

if __name__ == "__main__":
    alpha_dict = {}
    for i, c in zip(range(1, 27), string.ascii_lowercase):
        alpha_dict[c] = i
    L = int(input())
    _string = str(input())
    answer = 0
    for i, char in enumerate(_string):
        answer += alpha_dict[char] * pow(31, i, 1234567891)
    print(answer % 1234567891)
