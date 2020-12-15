if __name__ == "__main__":
    juice = list(map(int, input().split()))
    cocktail = list(map(int, input().split()))
    ratio = []
    for i in range(3):
        ratio.append(juice[i] / cocktail[i])
    for i in range(3):
        juice[i] = juice[i] - (cocktail[i] * min(ratio))
    for i in juice:
        if i == int(i):
            print(int(i), end=' ')
        else:
            print("%0.6f" % i, end=' ')