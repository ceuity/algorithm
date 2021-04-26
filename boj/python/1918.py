def solution():
    ops = str(input())
    answer = ''
    stack = []
    for char in ops:
        if char not in '+-*/()':
            answer += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
        elif char == '+' or char == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(char)
        elif char == '*' or char == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(char)
        else:
            stack.append(char)
    while stack:
        answer += stack.pop()
    print(answer)


if __name__ == "__main__":
    solution()