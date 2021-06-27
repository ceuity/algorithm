def check_balance(sentence: str):
    stack = []
    for char in sentence:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if not stack or stack.pop() != "(":
                return False
        elif char == "]":
            if not stack or stack.pop() != "[":
                return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    while True:
        sentence = input()
        if sentence == ".":
            break
        if check_balance(sentence):
            print("yes")
        else:
            print("no")
