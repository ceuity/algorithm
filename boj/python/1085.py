if __name__ == "__main__":
    x, y, w, h = map(int, input().split())
    print(min(abs(w-x), abs(h-y), abs(x), abs(y)))