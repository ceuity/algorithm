import itertools
import collections

def calculate_expressions(expressions, op):
    op = list(op)
    while len(expressions) != 1:
        curr_operation = op.pop()
        temp = collections.deque()
        while expressions:
            curr = expressions.popleft()
            if curr == curr_operation and curr == '*':
                temp.append(temp.pop() * expressions.popleft())
            elif curr == curr_operation and curr == '+':
                temp.append(temp.pop() + expressions.popleft())
            elif curr == curr_operation and curr == '-':
                temp.append(temp.pop() - expressions.popleft())
            else:
                temp.append(curr)
        expressions = temp
    return expressions[0]

def solution(expression):
    answer = 0
    expressions = collections.deque()
    operation = ['*', '+', '-']
    operations = itertools.permutations(operation, 3)
    temp = ''
    for e in expression:
        if e in operation:
            expressions.append(int(temp))
            expressions.append(e)
            temp = ''
        else:
            temp += e
    expressions.append(int(temp))
    for ops in operations:
        answer = max(answer, abs(calculate_expressions(expressions.copy(), ops)))
    return answer


if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))