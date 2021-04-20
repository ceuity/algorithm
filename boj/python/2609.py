if __name__ == "__main__":
    n, m = map(int, input().split())
    a, b = n, m
    while b:
        a, b = b, a % b
    gcd = a
    lcm = gcd * (n // a) * (m // a)
    print(gcd)
    print(lcm)
