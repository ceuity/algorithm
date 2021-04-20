if __name__ == "__main__":
    x = []
    y = []
    for _ in range(3):
        x1, y1 = map(int, input().split())
        if x1 in x:
            x.remove(x1)
        else:
            x.append(x1)
        if y1 in y:
            y.remove(y1)
        else:
            y.append(y1)
    print(x[0], y[0])