if __name__=="__main__":
    T = int(input())

    def check_vps(ps):
        stack = []
        for p in ps:
            if p == ')':
                if not stack:
                    return 'NO'
                elif stack[-1] != '(':
                    return 'NO'
                else:
                    stack.pop()
            else:
                stack.append(p)
        if stack:
            return 'NO'
        else:
            return 'YES'

    for _ in range(T):
        parenthesis = list(str(input()))
        print(check_vps(parenthesis))