if __name__ == "__main__":
    a, b, c, x, y = map(int, input().split())
    c *= 2
    result = 0
    if a > c and b > c:
        result = (c * (x - min(x, y))) + (c * (y - min(x, y))) + (c * min(x, y))
    elif (a + b) > c:
        if a > c:
            result = (c * (x - min(x, y))) + (b * (y - min(x, y))) + (c * min(x, y))
        elif b > c:
            result = (a * (x - min(x, y))) + (c * (y - min(x, y))) + (c * min(x, y))
        else:
            result = (a * (x - min(x, y))) + (b * (y - min(x, y))) + (c * min(x, y))
    else:
        result = (a * x) + (b * y)
    print(result)